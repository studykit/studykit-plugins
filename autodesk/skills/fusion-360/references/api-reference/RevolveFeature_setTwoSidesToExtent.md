# RevolveFeature.setTwoSidesToExtent Method

Parent Object: [RevolveFeature](RevolveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeature.h>

## Description

Changes the extent of the revolve to be defined as a two sided to extent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeature\_var" is a variable referencing a [RevolveFeature](RevolveFeature.htm) object.```` ``` returnValue = revolveFeature_var.setTwoSidesToExtent(toEntityOne, toEntityTwo) ``` ```` |

"revolveFeature\_var" is a variable referencing a [RevolveFeature](RevolveFeature.htm) object.  ```` ``` #include <Fusion/Features/RevolveFeature.h>  returnValue = revolveFeature_var->setTwoSidesToExtent(toEntityOne, toEntityTwo); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| toEntityOne | [Base](Base.htm) | The first entity that defines the "to" extent. The valid types of entities can vary depending on the type of feature this is being used with. For a revolve it can be a BRepBody, BRepFace, BRepVertex, ConstructionPlane, or ConstructionPoint. |
| toEntityTwo | [Base](Base.htm) | The second entity that defines the "to" extent. The valid types of entities can vary depending on the type of feature this is being used with. For a revolve it can be a BRepBody, BRepFace, BRepVertex, ConstructionPlane, or ConstructionPoint. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |