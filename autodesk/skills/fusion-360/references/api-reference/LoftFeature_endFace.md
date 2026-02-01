# LoftFeature.endFace Property

Parent Object: [LoftFeature](LoftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeature.h>

## Description

Property that returns the face that caps the end of the loft and is coincident with the last section. In the case where the loft isn't capped and there isn't an end face, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeature\_var" is a variable referencing a LoftFeature object. |

"loftFeature\_var" is a variable referencing a LoftFeature object. ```` ``` #include <Fusion/Features/LoftFeature.h>  // Get the value of the property. Ptr<BRepFace> propertyValue = loftFeature_var->endFace(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFace](BRepFace.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |