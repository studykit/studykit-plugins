# CreateFromCAMTemplateInput.camTemplate Property

Parent Object: [CreateFromCAMTemplateInput](CreateFromCAMTemplateInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CreateFromCAMTemplateInput.h>

## Description

Gets and sets the template to be instantiated.

## Syntax

* [Python](#Python)
* [C++](#C++)

"createFromCAMTemplateInput\_var" is a variable referencing a CreateFromCAMTemplateInput object. |

"createFromCAMTemplateInput\_var" is a variable referencing a CreateFromCAMTemplateInput object. ```` ``` #include <Cam/CAM/CreateFromCAMTemplateInput.h>  // Get the value of the property. Ptr<CAMTemplate> propertyValue = createFromCAMTemplateInput_var->camTemplate();  // Set the value of the property, where value_var is a CAMTemplate. bool returnValue = createFromCAMTemplateInput_var->camTemplate(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CAMTemplate](CAMTemplate.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Additive Manufacturing SLA API Sample](AdditiveSLAManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive SLA manufacturing setup.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.  The setup will select a SLA 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected SLA machine. This script will also create support structures, based on the orientation of each component.  The support and orientation operations are created from a template. The script further demonstrates how to wrap script code into a command such that only one undo entry is created for the entire script instead of one entry per internal action. |

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |