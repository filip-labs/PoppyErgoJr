# GitHub presentation settings

Repository settings are separate from versioned files and are not applied by
merging a pull request. The connected GitHub tools can update files and PRs but
do not expose repository metadata or social-preview writes. These fields were
empty at review; the browser was signed out.

## About

On the repository's Code page, use the gear next to **About**. Set:

- Description: `Computer vision-powered color-sorting and pick-and-place prototype built with Poppy Ergo Jr and Python.`
- Website: `https://www.filipzcvetkovic.com`
- Topics (space-separated):

```text
robotics poppy-ergo-jr computer-vision python robot-control pick-and-place robotic-arm automation hardware-software-integration opencv
```

Save changes. The wording reflects the fixed-pose educational implementation;
it does not imply a general-purpose manipulation or production control system.
All ten topics correspond to the existing camera/vision/motor workflow.

## Social preview

Upload `docs/assets/social-preview.png` from this branch under **Settings →
General → Social preview → Edit → Upload an image**. Merely committing the PNG
does not activate GitHub's social preview.

GitHub recommends 1280 × 640 pixels and a PNG/JPG/GIF below 1 MB:
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview

Design: dark navy, off-white typography and restrained abstract joint marks.
Title: PoppyErgoJr. Subtitle: Computer Vision & Robotic Manipulation.
The graphic is a generated design concept, not a photograph, robot model or
technical schematic. No external robot photograph is republished.

## Branch and release status

The README's CI badge intentionally targets `improvement/professional-repository`
while its workflow is pending merge. After merging, change both badge and link
branch filters to `main`. Until then, the public default-branch README remains
unchanged. Do not merge automatically.

No tags or releases were present at review. No release or version has been
invented for a presentation-only update. Establish a first tagged release after
recording a reproducible hardware environment and completing supervised checks.
The repository name and licensing terms remain unchanged.

## Image generation specification

Created with the built-in image generation tool; resized and optimized for upload.

```text
Create a professional GitHub social preview raster image at EXACTLY 1280 by 640 pixels, 2:1 ratio. Minimalist editorial engineering graphic. Solid dark navy #121B26 background, warm off-white text, muted slate thin lines. Left aligned title text exactly "PoppyErgoJr" large clean modern sans serif, subtitle exactly "Computer Vision & Robotic Manipulation". Small footer text exactly "Python / OpenCV / Pypot" and "filipzcvetkovic.com". Generous whitespace and 80px safe margins. Right side has only a very restrained abstract arrangement of thin joint circles and short connecting lines, plus two tiny red and blue square accents referencing color sorting; clearly graphic design rather than a depiction of an actual robot or architecture diagram. No robot rendering, no photographs, no gradients, no glow, no shadows, no logos, no badges, no additional text, no decorative banner framing. Crisp and understated, designed for a serious robotics software repository.
```
