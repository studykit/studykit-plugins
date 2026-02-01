# MirrorFeature.patternComputeOption Property

Parent Object: [MirrorFeature](MirrorFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeature.h>

## Description

Gets and sets the compute option for this mirror feature. This property only applies when mirroring features and is ignored in the direct modeling environment.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeature\_var" is a variable referencing a MirrorFeature object.  ```` ``` # Get the value of the property. propertyValue = mirrorFeature_var.patternComputeOption  # Set the value of the property. mirrorFeature_var.patternComputeOption = propertyValue ``` ```` |

"mirrorFeature\_var" is a variable referencing a MirrorFeature object. ```` ``` #include <Fusion/Features/MirrorFeature.h>  // Get the value of the property. PatternComputeOptions propertyValue = mirrorFeature_var->patternComputeOption();  // Set the value of the property, where value_var is a PatternComputeOptions. bool returnValue = mirrorFeature_var->patternComputeOption(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PatternComputeOptions](PatternComputeOptions.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |