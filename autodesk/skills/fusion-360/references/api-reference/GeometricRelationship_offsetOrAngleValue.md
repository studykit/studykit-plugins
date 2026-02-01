# GeometricRelationship.offsetOrAngleValue Property![](../images/TestTubeLarge.png)

Parent Object: [GeometricRelationship](GeometricRelationship.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/GeometricRelationship.h>

## Description

This property is used when creating a new joint or assembly constraint and defines the offset or angle associated with this geometric relationship. The value defaults to 0, but can be set with a ValueInput defining a length or angle. It can be either a real value, which will be in centimeters or radians, or a string, which is an expression whose units are length or angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"geometricRelationship\_var" is a variable referencing a GeometricRelationship object. |

"geometricRelationship\_var" is a variable referencing a GeometricRelationship object. ```` ``` #include <Fusion/Components/GeometricRelationship.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = geometricRelationship_var->offsetOrAngleValue();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = geometricRelationship_var->offsetOrAngleValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |