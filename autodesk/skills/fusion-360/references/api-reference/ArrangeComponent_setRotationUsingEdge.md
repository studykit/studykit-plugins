# ArrangeComponent.setRotationUsingEdge Method

Parent Object: [ArrangeComponent](ArrangeComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponent.h>

## Description

Sets the rotation angle using the specified edge such that the edge is pointing in the zero rotation angle. This is a convenience method to set the rotation angle. The rotation property can be used to accomplish the same result.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponent\_var" is a variable referencing an [ArrangeComponent](ArrangeComponent.htm) object.```` ``` returnValue = arrangeComponent_var.setRotationUsingEdge(edge) ``` ```` |

"arrangeComponent\_var" is a variable referencing an [ArrangeComponent](ArrangeComponent.htm) object.  ```` ``` #include <Fusion/Arrange/ArrangeComponent.h>  returnValue = arrangeComponent_var->setRotationUsingEdge(edge); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edge | [BRepEdge](BRepEdge.htm) | The BRepEdge object being used to define rotation of the component. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |