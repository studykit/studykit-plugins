# Machine Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Machine/Machine.h>

## Description

Object that represents a machine.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Machine_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [clearSimulationModel](Machine_clearSimulationModel.htm) | ![Preview](../images/TestTubeSmall.png)Clears the simulation model from the machine. |
| [create](Machine_create.htm) | Creates a machine from a "MachineInput" input object |
| [equivalentTo](Machine_equivalentTo.htm) | Checks if the machine is equivalent to this one. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [capabilities](Machine_capabilities.htm) | Gets the capabilities of the machine. |
| [description](Machine_description.htm) | Gets and sets the description of the machine. |
| [elements](Machine_elements.htm) | Gets the list of elements that make up this machine. |
| [hasPost](Machine_hasPost.htm) | Checks if the machine has a post. |
| [hasSimulationModel](Machine_hasSimulationModel.htm) | ![Preview](../images/TestTubeSmall.png)Returns true if the machine has a simulation model attached. |
| [id](Machine_id.htm) | Gets the unique identifier of the machine. Can be used for comparing machines within the document. |
| [isValid](Machine_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [model](Machine_model.htm) | Gets and sets the model name of the machine. |
| [objectType](Machine_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [postURL](Machine_postURL.htm) | Gets or sets the URL of the post assigned to the machine. |
| [vendor](Machine_vendor.htm) | Gets and sets the vendor name of the machine. |

## Accessed From

[CAM.allMachines](CAM_allMachines.htm), [Machine.create](Machine_create.htm), [MachineLibrary.childMachines](MachineLibrary_childMachines.htm), [MachineLibrary.machineAtURL](MachineLibrary_machineAtURL.htm), [MachineQuery.execute](MachineQuery_execute.htm), [NCProgram.machine](NCProgram_machine.htm), [PrintSettingQuery.machine](PrintSettingQuery_machine.htm), [Setup.machine](Setup_machine.htm), [SetupInput.machine](SetupInput_machine.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Additive Manufacturing FFF API Sample](AdditiveFFFManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive FFF manufacturing setup and generate a toolpath.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.  The setup will select an FFF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected FFF machine. This script will also create support structures, if required, based on the orientation of each component. Finally, the script generates the toolpath for the active setup and lets the user choose if they wish to post process the resulting toolpath or if they want to simulate it. |
| [Additive Manufacturing MJF API Sample](AdditiveMJFManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.  The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine. |
| [Additive Manufacturing SLA API Sample](AdditiveSLAManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive SLA manufacturing setup.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.  The setup will select a SLA 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected SLA machine. This script will also create support structures, based on the orientation of each component.  The support and orientation operations are created from a template. The script further demonstrates how to wrap script code into a command such that only one undo entry is created for the entire script instead of one entry per internal action. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |