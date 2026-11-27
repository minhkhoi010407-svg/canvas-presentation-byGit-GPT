import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const errors = [];
const requiredFiles = [
  "README.md",
  "MASTER_GUIDE.md",
  "INTEGRATION_MANIFEST.md",
  "SOURCE_REGISTRY.json",
  "LICENSES.md",
  ".github/copilot-instructions.md",
  "00-CORE/PRESENTATION_WORKFLOW.md",
  "06-UNIFIED-ENGINE/SKILL_ROUTER.md",
  "08-REFERENCE/DEPENDENCY_MATRIX.md",
];
const expectedSourceUrls = new Set([
  "https://github.com/gnipbao/knowledge-cat-ppt-skill",
  "https://github.com/qybaihe/codex-ppt",
  "https://github.com/siril9/presentation-skill",
  "https://github.com/shaikaakif/Master-Slide-Skill",
  "https://github.com/hiamberhuang/presentation-agent-skills",
  "https://github.com/gitbrent/PptxGenJS",
  "https://github.com/Ziv-Barber/officegen",
  "https://github.com/marp-team/marp",
  "https://github.com/slidevjs/slidev",
  "https://github.com/microsoft/playwright",
  "https://github.com/shadcn-ui/ui",
  "https://github.com/lucide-icons/lucide",
]);

function walk(directory) {
  const found = [];
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (entry.name === ".git") continue;
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) found.push(...walk(fullPath));
    else found.push(fullPath);
  }
  return found;
}

for (const relativePath of requiredFiles) {
  if (!fs.existsSync(path.join(root, relativePath))) errors.push(`Missing required file: ${relativePath}`);
}

const registryPath = path.join(root, "SOURCE_REGISTRY.json");
let registry;
try {
  registry = JSON.parse(fs.readFileSync(registryPath, "utf8"));
  const sources = registry.sources;
  if (!Array.isArray(sources) || sources.length !== 12) {
    errors.push(`Expected exactly 12 registry sources; found ${Array.isArray(sources) ? sources.length : "non-array"}`);
  } else {
    const ids = sources.map((source) => source.id);
    if (new Set(ids).size !== 12) errors.push("Registry source IDs are not unique");
    const urls = new Set(sources.map((source) => source.url));
    if (urls.size !== 12 || [...expectedSourceUrls].some((url) => !urls.has(url))) {
      errors.push("Registry source URLs do not match the requested set of 12 repositories");
    }
    for (const source of sources) {
      if (!source.name || !source.url || !source.license || !source.inclusion || !source.source_path || !source.license_file) {
        errors.push(`Incomplete registry record: ${source.id ?? "(missing id)"}`);
      }
      if (!/^[0-9a-f]{40}$/i.test(source.latest_verified_commit ?? "")) {
        errors.push(`Invalid verified commit SHA for ${source.id}`);
      }
      if (source.source_commit !== null && !/^[0-9a-f]{40}$/i.test(source.source_commit)) {
        errors.push(`Invalid source commit SHA for ${source.id}`);
      }
      if (!["curated-source", "reference-only"].includes(source.integration_level)) {
        errors.push(`Invalid integration level for ${source.id}: ${source.integration_level ?? "(missing)"}`);
      }
      const sourceDirectory = path.join(root, source.source_path);
      if (!fs.existsSync(path.join(sourceDirectory, "README.md"))) {
        errors.push(`Missing source guide for ${source.id}: ${source.source_path}/README.md`);
      }
      if (!fs.existsSync(path.join(sourceDirectory, source.license_file))) {
        errors.push(`Missing source license for ${source.id}: ${source.source_path}/${source.license_file}`);
      }
      if (source.id === "playwright" && !fs.existsSync(path.join(sourceDirectory, "NOTICE"))) {
        errors.push("Missing preserved Playwright NOTICE");
      }
    }
  }
} catch (error) {
  errors.push(`Invalid SOURCE_REGISTRY.json: ${error.message}`);
}

const files = walk(root);
const forbiddenDirectories = new Set(["node_modules", "__pycache__", ".pytest_cache", ".venv", "coverage", "dist"]);
for (const fullPath of files) {
  const relativePath = path.relative(root, fullPath);
  if (relativePath.split(path.sep).some((part) => forbiddenDirectories.has(part))) {
    errors.push(`Forbidden generated/dependency path: ${relativePath}`);
  }
  if (/\.(pem|p12|pfx|key)$/i.test(relativePath) || /\.env(?:\.|$)/i.test(path.basename(relativePath))) {
    errors.push(`Potential secret/credential file: ${relativePath}`);
  }
}

for (const fullPath of files.filter((file) => file.toLowerCase().endsWith(".json"))) {
  try {
    JSON.parse(fs.readFileSync(fullPath, "utf8"));
  } catch (error) {
    errors.push(`Invalid JSON ${path.relative(root, fullPath)}: ${error.message}`);
  }
}

const lucideLicensePath = path.join(root, "04-UI-AND-VISUAL", "lucide", "LICENSE");
if (fs.existsSync(lucideLicensePath)) {
  const lucideLicense = fs.readFileSync(lucideLicensePath, "utf8");
  if (!lucideLicense.includes("ISC License") || !lucideLicense.includes("The MIT License (MIT) (for the icons listed above)")) {
    errors.push("Lucide license does not retain both the ISC terms and Feather-derived MIT terms");
  }
}

function markdownLinks(text) {
  const links = [];
  const pattern = /\[[^\]]*\]\(([^)]+)\)/g;
  for (const match of text.matchAll(pattern)) {
    const target = match[1].trim().replace(/^<|>$/g, "");
    if (!target || target.startsWith("#") || /^[a-z][a-z0-9+.-]*:/i.test(target) || target.startsWith("//")) continue;
    links.push(target);
  }
  return links;
}

for (const fullPath of files.filter((file) => file.toLowerCase().endsWith(".md"))) {
  const relativePath = path.relative(root, fullPath);
  const text = fs.readFileSync(fullPath, "utf8");
  for (const link of markdownLinks(text)) {
    const pathname = decodeURIComponent(link.split("#", 1)[0].split("?", 1)[0]);
    if (!pathname) continue;
    const target = path.resolve(path.dirname(fullPath), pathname);
    if (!target.startsWith(`${root}${path.sep}`) && target !== root) {
      errors.push(`Link escapes repository: ${relativePath} -> ${link}`);
    } else if (!fs.existsSync(target)) {
      errors.push(`Broken local link: ${relativePath} -> ${link}`);
    }
  }
}

if (errors.length) {
  console.error(`Repository validation failed (${errors.length} issue${errors.length === 1 ? "" : "s"}):`);
  for (const error of errors) console.error(`- ${error}`);
  process.exitCode = 1;
} else {
  console.log(`Repository validation passed: ${registry.sources.length} sources, ${files.length} files, local links resolved.`);
}

