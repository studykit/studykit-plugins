# StringParameterValue.value Property

Parent Object: [StringParameterValue](StringParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/StringParameterValue.h>

## Description

Get or set the value of the parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stringParameterValue\_var" is a variable referencing a StringParameterValue object. |

"stringParameterValue\_var" is a variable referencing a StringParameterValue object. ```` ``` #include <Cam/Operations/StringParameterValue.h>  // Get the value of the property. string propertyValue = stringParameterValue_var->value();  // Set the value of the property, where value_var is a string. bool returnValue = stringParameterValue_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Additive Manufacturing MJF API Sample](AdditiveMJFManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.  The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine. |

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |