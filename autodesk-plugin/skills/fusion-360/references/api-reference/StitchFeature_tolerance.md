# StitchFeature.tolerance Property

Parent Object: [StitchFeature](StitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeature.h>

## Description

Returns the parameter controlling the tolerance. You can edit the tolerance by editing the value of the parameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeature\_var" is a variable referencing a StitchFeature object. |

"stitchFeature\_var" is a variable referencing a StitchFeature object. ```` ``` #include <Fusion/Features/StitchFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = stitchFeature_var->tolerance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |