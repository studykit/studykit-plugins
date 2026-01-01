# FilletEdgeSet.tangencyWeight Property

Parent Object: [FilletEdgeSet](FilletEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSet.h>

## Description

Returns the model parameter that controls the G1 or G2 tangency weight of the fillet. It must be a real value between 0.1 and 2.0 inclusive. You can edit the tangency weight by using the properties on the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletEdgeSet\_var" is a variable referencing a FilletEdgeSet object. |

"filletEdgeSet\_var" is a variable referencing a FilletEdgeSet object. ```` ``` #include <Fusion/Features/FilletEdgeSet.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = filletEdgeSet_var->tangencyWeight(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |