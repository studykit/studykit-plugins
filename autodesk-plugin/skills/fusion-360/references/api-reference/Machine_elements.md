# Machine.elements Property

Parent Object: [Machine](Machine.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/Machine.h>

## Description

Gets the list of elements that make up this machine.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machine\_var" is a variable referencing a Machine object. |

"machine\_var" is a variable referencing a Machine object. ```` ``` #include <Cam/Machine/Machine.h>  // Get the value of the property. Ptr<MachineElements> propertyValue = machine_var->elements(); ``` ```` |

## Property Value

This is a read only property whose value is a [MachineElements](MachineElements.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Additive Manufacturing MJF API Sample](AdditiveMJFManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.  The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |