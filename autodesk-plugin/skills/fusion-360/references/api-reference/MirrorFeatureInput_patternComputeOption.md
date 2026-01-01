# MirrorFeatureInput.patternComputeOption Property

Parent Object: [MirrorFeatureInput](MirrorFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeatureInput.h>

## Description

Gets and sets the compute option when mirroring features. The default value for this is AdjustPatternCompute. This property only applies when mirroring features and is ignored in the direct modeling environment.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeatureInput\_var" is a variable referencing a MirrorFeatureInput object. |

"mirrorFeatureInput\_var" is a variable referencing a MirrorFeatureInput object. ```` ``` #include <Fusion/Features/MirrorFeatureInput.h>  // Get the value of the property. PatternComputeOptions propertyValue = mirrorFeatureInput_var->patternComputeOption();  // Set the value of the property, where value_var is a PatternComputeOptions. bool returnValue = mirrorFeatureInput_var->patternComputeOption(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PatternComputeOptions](PatternComputeOptions.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |