# Setup for a consuming application

This repository is reference material and has no root application dependencies to install.

1. Choose one lane (native PPTX, image-first, Marp, or Slidev).
2. Select the corresponding upstream package and version from its current documentation; add it to the application, not this toolkit.
3. Check runtime, renderer, browser, font, and export prerequisites on the target host.
4. Pin dependencies with that application’s package manager and retain its lockfile.
5. Add application-level adapter tests and preserve the generated artifact, render receipt, and QA report.
6. Inventory the installed packages' licenses and transitive dependencies before redistribution.

Do not install the optional skills' full dependencies just to read their instructions. Do not assume Google AI Studio provides external rendering executables or persistent storage.

