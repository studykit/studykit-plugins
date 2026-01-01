# OptimizedOrientationResults.currentOrientationResult Property

Parent Object: [OptimizedOrientationResults](OptimizedOrientationResults.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeneratedData/OptimizedOrientationResults.h>

## Description

Gets or sets the desired OrientationResult. When setting, the orientation matrix is applied to the component selected in the parent orientation operation, possibly invalidating other operations.

## Syntax

* [Python](#Python)
* [C++](#C++)

"optimizedOrientationResults\_var" is a variable referencing an OptimizedOrientationResults object. |

"optimizedOrientationResults\_var" is a variable referencing an OptimizedOrientationResults object. ```` ``` #include <Cam/GeneratedData/OptimizedOrientationResults.h>  // Get the value of the property. Ptr<OptimizedOrientationResult> propertyValue = optimizedOrientationResults_var->currentOrientationResult();  // Set the value of the property, where value_var is an OptimizedOrientationResult. bool returnValue = optimizedOrientationResults_var->currentOrientationResult(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [OptimizedOrientationResult](OptimizedOrientationResult.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Additive Manufacturing FFF API Sample](AdditiveFFFManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive FFF manufacturing setup and generate a toolpath.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.  The setup will select an FFF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected FFF machine. This script will also create support structures, if required, based on the orientation of each component. Finally, the script generates the toolpath for the active setup and lets the user choose if they wish to post process the resulting toolpath or if they want to simulate it. |
| [Additive Manufacturing SLA API Sample](AdditiveSLAManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive SLA manufacturing setup.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.  The setup will select a SLA 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected SLA machine. This script will also create support structures, based on the orientation of each component.  The support and orientation operations are created from a template. The script further demonstrates how to wrap script code into a command such that only one undo entry is created for the entire script instead of one entry per internal action. |

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |