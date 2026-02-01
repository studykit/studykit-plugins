# StitchFeatureInput.tolerance Property

Parent Object: [StitchFeatureInput](StitchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeatureInput.h>

## Description

Gets and sets the ValueInput object that defines the stitching tolerance. It must define a length.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeatureInput\_var" is a variable referencing a StitchFeatureInput object. |

"stitchFeatureInput\_var" is a variable referencing a StitchFeatureInput object. ```` ``` #include <Fusion/Features/StitchFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = stitchFeatureInput_var->tolerance();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = stitchFeatureInput_var->tolerance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |