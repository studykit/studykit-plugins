# ArrangeComponents.add Method

Parent Object: [ArrangeComponents](ArrangeComponents.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeComponents.h>

## Description

Adds a new ArrangeComponent object to the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeComponents\_var" is a variable referencing an [ArrangeComponents](ArrangeComponents.htm) object.```` ``` returnValue = arrangeComponents_var.add(occurrenceOrFace) ``` ```` |

"arrangeComponents\_var" is a variable referencing an [ArrangeComponents](ArrangeComponents.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ArrangeComponent](ArrangeComponent.htm) | Returns the created ArrangeComponent where you can use properties on it to define the various other settings supported to control how the component is arranged. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrenceOrFace | [Base](Base.htm) | For a 2D arrange this can be an Occurrence or BRepFace object that defines which component to use. If a BRepFace object is used, the face is used to orient the part in the arrangement and will face up or down depending on the isGlobalDirectionFaceUp property on the ArrangeFeature2DInput object.   For a 2D arrange, if an Occurrence is provided, the Occurrence will be oriented in the arrangement such that the largest face points downward.   For a 3D arrange this can be an Occurrence or BRepFace object but if a BRepFace is provided it does not define the orientation but is only used to get the parent Occurrence. For a 3D arrange the arranged occurrences have the same orientation as the original occurrence but are positioned within the 3D envelope. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |