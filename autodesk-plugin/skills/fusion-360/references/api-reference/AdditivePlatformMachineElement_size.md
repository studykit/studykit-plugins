# AdditivePlatformMachineElement.size Property

Parent Object: [AdditivePlatformMachineElement](AdditivePlatformMachineElement.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/AdditivePlatformMachineElement.h>

## Description

Usable platform size. Units are cm.

## Syntax

* [Python](#Python)
* [C++](#C++)

"additivePlatformMachineElement\_var" is a variable referencing an AdditivePlatformMachineElement object. |

"additivePlatformMachineElement\_var" is a variable referencing an AdditivePlatformMachineElement object. ```` ``` #include <Cam/Machine/AdditivePlatformMachineElement.h>  // Get the value of the property. Ptr<Point3D> propertyValue = additivePlatformMachineElement_var->size();  // Set the value of the property, where value_var is a Point3D. bool returnValue = additivePlatformMachineElement_var->size(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Additive Manufacturing MJF API Sample](AdditiveMJFManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.  The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine. |

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |