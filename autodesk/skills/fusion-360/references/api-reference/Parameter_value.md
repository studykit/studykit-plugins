# Parameter.value Property

Parent Object: [Parameter](Parameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Parameter.h>

## Description

Gets and sets the real value (a double) of the parameter in database units. Setting this property will set/reset the expression value for this parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameter\_var" is a variable referencing a Parameter object.  ```` ``` # Get the value of the property. propertyValue = parameter_var.value  # Set the value of the property. parameter_var.value = propertyValue ``` ```` |

"parameter\_var" is a variable referencing a Parameter object. ```` ``` #include <Fusion/Fusion/Parameter.h>  // Get the value of the property. double propertyValue = parameter_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = parameter_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Animation API Sample](CreateAnimation_Sample.htm) | Creates a series of images of a design where a parameter is being changed. The series of images can be used to create an animation using other software. To run this sample, have a part open that contains a parameter named "Length". The parameter should be able to be successfully modified from 10 to 15 centimeters. Run the sample and choose or create a directory for the output. After running you should have a folder full of images that are snapshots of each parameter value. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |