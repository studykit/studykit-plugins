# GeometricRelationship.entityOne Property![](../images/TestTubeLarge.png)

Parent Object: [GeometricRelationship](GeometricRelationship.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/GeometricRelationship.h>

## Description

Gets and sets the first entity in the relationship. The entity can be a BRepFace, BRepedge, BRepVertex, SketchPoint, SketchCurve, ConstructionPlane, ConstructionAxis, or ConstructionPoint object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricRelationship\_var" is a variable referencing a GeometricRelationship object. |

"geometricRelationship\_var" is a variable referencing a GeometricRelationship object. ```` ``` #include <Fusion/Components/GeometricRelationship.h>  // Get the value of the property. Ptr<Base> propertyValue = geometricRelationship_var->entityOne();  // Set the value of the property, where value_var is a Base. bool returnValue = geometricRelationship_var->entityOne(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |