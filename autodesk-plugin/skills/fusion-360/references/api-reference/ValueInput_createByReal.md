# ValueInput.createByReal Method

Parent Object: [ValueInput](ValueInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ValueInput.h>

## Description

Creates a new ValueInput object using a double. For example, if you create a value using the double value 2 and use it as input for a length, it will be interpreted as 2 cm because centimeters are the internal unit for length. Values defined by a real are always interpreted to be in the appropriate internal unit. For example, if the value 2 is used to define the depth of an extrusion (a length value), it will be 2 cm because cm is the internal unit for lengths. If the value 2 is used to define the angle of the extrude, it will be 2 radians because radians are the internal unit for angles.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ValueInput](ValueInput.htm) | Returns the newly created ValueInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| realValue | double | a double value |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |