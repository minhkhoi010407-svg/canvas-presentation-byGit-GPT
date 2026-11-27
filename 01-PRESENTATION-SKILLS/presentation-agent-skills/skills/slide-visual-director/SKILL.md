---
name: slide-visual-director
description: Art-direct and produce presentation visuals such as cover images, section heroes, editorial collages, conceptual illustrations, product scenes, and diagram assets with slide-safe composition and consistent visual language. Use when a presentation needs generated or sourced imagery; do not use for charts, text-heavy diagrams, or data that should remain editable native slide objects.
license: MIT
metadata:
  short-description: Slide-safe art direction and presentation image prompts
---

# Slide Visual Director

Create visuals that clarify the slide's message and survive the actual crop, title placement, and room-viewing conditions of a presentation.

## Decide whether an image is the right tool

Use generated or photographic imagery for atmosphere, metaphor, product context, editorial storytelling, and complex scenes. Use native slide shapes for charts, processes, matrices, labels, and evidence that must stay accurate or editable. Never rasterize a simple diagram merely to make it look polished.

## Visual brief

Before producing an asset, establish:

- slide message and audience;
- asset role: cover, section divider, proof, product scene, background, or decorative support;
- subject and required real-world details;
- tone, medium, palette, lighting, lens or perspective, and texture;
- final slide aspect ratio and the asset's on-slide rectangle;
- title, subtitle, logo, or chart exclusion zones;
- whether transparency, safe cropping, or multiple variants are required.

If the deck already has approved pages, derive an art-direction system from them instead of inventing a new style for each image.

## Composition rules

- Design for the final placement, not as a standalone poster.
- Reserve deliberate negative space behind overlaid text.
- Put the subject's visual weight opposite the main text block unless centered symmetry is intentional.
- Keep critical faces, products, and gestures away from crop boundaries.
- Avoid high-frequency detail behind small labels.
- Generate wide when the image spans a slide; do not stretch a portrait asset into 16:9.
- Ask for text-free output by default. Add slide copy as native text for accuracy and editability.

## Consistency across a deck

Lock a small set of repeatable decisions: color temperature, contrast, camera distance, depth of field, material treatment, illustration grammar, and grain. Vary subject and composition while preserving those decisions.

Do not mix photorealism, clay 3D, flat vector, anime, and corporate stock photography in the same narrative unless the contrast is conceptually required.

## Prompt contract

A useful prompt contains:

1. asset role and slide message;
2. main subject and action;
3. environment and supporting details;
4. composition and negative-space direction;
5. medium, lighting, palette, camera, and texture;
6. aspect ratio and crop constraints;
7. exclusions such as embedded text, watermarks, fake logos, UI gibberish, or extra subjects.

Read [references/prompt-recipes.md](references/prompt-recipes.md) for reusable prompt structures.

## Brand and evidence safety

- Use official logos and product screenshots supplied by the user; do not ask an image model to redraw them.
- Do not fabricate customer settings, product capabilities, awards, interfaces, or people presented as real.
- Label conceptual or illustrative scenes when a reasonable viewer could mistake them for evidence.
- Confirm usage rights and attribution requirements for sourced images.
- Keep charts, numerical claims, and citations outside generated imagery.

## QA

Review the visual at both full-screen and thumbnail size. Check subject anatomy, object count, brand details, perspective, lighting consistency, empty-space usability, crop resilience, contrast under text, and coherence with adjacent slides.

Deliver the final asset, the prompt or source record, intended slide placement, crop guidance, and any unresolved authenticity or licensing limitation.
