# MirrorFeatureInput.stitchTolerance Property

Parent Object: [MirrorFeatureInput](MirrorFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeatureInput.h>

## Description

Gets and sets the ValueInput object that defines the Stitching Tolerance (length) to use when doing a mirror and combine for surface bodies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeatureInput\_var" is a variable referencing a MirrorFeatureInput object. |

"mirrorFeatureInput\_var" is a variable referencing a MirrorFeatureInput object. ```` ``` #include <Fusion/Features/MirrorFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = mirrorFeatureInput_var->stitchTolerance();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = mirrorFeatureInput_var->stitchTolerance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |