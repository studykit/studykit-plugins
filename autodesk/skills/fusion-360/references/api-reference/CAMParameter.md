# CAMParameter Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMParameter.h>

## Description

Base class for representing parameter of an operation.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CAMParameter_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [saveExpressionAsUserDefault](CAMParameter_saveExpressionAsUserDefault.htm) | ![Preview](../images/TestTubeSmall.png)Saves the current expression as user default value. Throws an exception if the parent is not an operation or does not support user default expressions. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [error](CAMParameter_error.htm) | Returns a message corresponding to any active error associated with the value of this parameter. |
| [expression](CAMParameter_expression.htm) | Gets and sets the value expression of the parameter. |
| [fullTitle](CAMParameter_fullTitle.htm) | ![Preview](../images/TestTubeSmall.png)Returns the full title of this parameter as seen in the user interface. This can potentially be more descriptive than the basic title. This title is localized and can change based on the current language. |
| [isDeprecated](CAMParameter_isDeprecated.htm) | Gets if this parameter is deprecated. Some parameters are deprecated when their usage becomes obsolete. Reading deprecated parameters is allowed, but setting deprecated parameters will throw an error. |
| [isEditable](CAMParameter_isEditable.htm) | Returns whether or not the parameter's expression or value can be modified. |
| [isEnabled](CAMParameter_isEnabled.htm) | Gets if this parameter is enabled. Some parameters are enabled/disabled depending on the values set for other parameters. |
| [isValid](CAMParameter_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](CAMParameter_isVisible.htm) | ![Preview](../images/TestTubeSmall.png)Gets if this parameter is visible in the user interface. |
| [name](CAMParameter_name.htm) | Gets the name (internal name) of the parameter. |
| [objectType](CAMParameter_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [systemDefaultExpression](CAMParameter_systemDefaultExpression.htm) | ![Preview](../images/TestTubeSmall.png)Returns the systemDefaultExpression of this parameter. |
| [title](CAMParameter_title.htm) | Returns the title of this parameter as seen in the user interface. This title is localized and can change based on the current language |
| [userDefaultExpression](CAMParameter_userDefaultExpression.htm) | ![Preview](../images/TestTubeSmall.png)Gets and sets the userDefaultExpression of this parameter. If no userDefaultExpression is set, the systemDefaultExpression is returned. Throws an exception if the parent is not an operation or does not support user default expressions. |
| [value](CAMParameter_value.htm) | Returns an object that allows you to get and set the value associated with the parameter. |
| [warning](CAMParameter_warning.htm) | Returns a message corresponding to any active warning associated with the value of this parameter. |

## Accessed From

[CAMParameters.item](CAMParameters_item.htm), [CAMParameters.itemByName](CAMParameters_itemByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Additive Manufacturing FFF API Sample](AdditiveFFFManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive FFF manufacturing setup and generate a toolpath.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.  The setup will select an FFF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected FFF machine. This script will also create support structures, if required, based on the orientation of each component. Finally, the script generates the toolpath for the active setup and lets the user choose if they wish to post process the resulting toolpath or if they want to simulate it. |
| [Additive Manufacturing MJF API Sample](AdditiveMJFManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.  The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine. |
| [Additive Manufacturing SLA API Sample](AdditiveSLAManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive SLA manufacturing setup.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.  The setup will select a SLA 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected SLA machine. This script will also create support structures, based on the orientation of each component.  The support and orientation operations are created from a template. The script further demonstrates how to wrap script code into a command such that only one undo entry is created for the entire script instead of one entry per internal action. |
| [CAM Parameter Modification API Sample](CAMParameterChange_Sample_Sample.htm) | Demonstrates changing parameters of existing toolpaths. |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |