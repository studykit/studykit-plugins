# Parameter.expression Property

Parent Object: [Parameter](Parameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Parameter.h>

## Description

Gets and sets the expression used to calculate the value of the parameter. This is the equivalent of the "Expression" column in the Parameters dialog. Numeric parameters can be defined by a simple expression like "6.25", which will be interpreted based on whatever the default units are for the document. For example, if the units are set to millimeters, the value will be 6.25 mm; if the units are inches, it will be 6.25 inches. The expression can also contain the units so "6.25 in" will always be evaluated as inches regardless of the document units.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameter\_var" is a variable referencing a Parameter object.  ```` ``` # Get the value of the property. propertyValue = parameter_var.expression  # Set the value of the property. parameter_var.expression = propertyValue ``` ```` |

"parameter\_var" is a variable referencing a Parameter object. ```` ``` #include <Fusion/Fusion/Parameter.h>  // Get the value of the property. string propertyValue = parameter_var->expression();  // Set the value of the property, where value_var is a string. bool returnValue = parameter_var->expression(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Set parameters from a csv file and export to STEP](SetParametersFromACsvFileAndExportToSTEP_Sample.htm) | Reads data from a .csv file and sets user parameters in the model and then exports the model to STEP. When setting parameters be aware that this sample is setting user parameters. It's also possible to set model parameters but that's not demonstrated here. Also when accessing parameters, it is case sensitive so the names you use in your program much exactly match the names in the model. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |