# GeneratedDataCollection Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/GeneratedData/GeneratedDataCollection.h>

## Description

Collection can hold multiple GeneratedData results for a particular operation, setup or folder. In the case of folders and setups, the data associated with the child operations is not added to the collection. In most cases folders and setups will not have any items in the collection, whereas most operations will only have one.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](GeneratedDataCollection_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](GeneratedDataCollection_item.htm) | Gets the desired generated data at the given index. |
| [itemByIdentifier](GeneratedDataCollection_itemByIdentifier.htm) | Gets the desired generated data. Generated result objects are unique for a given identifier, but may contain any number of child objects. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](GeneratedDataCollection_count.htm) | The number of items in the collection. |
| [isValid](GeneratedDataCollection_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](GeneratedDataCollection_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAMAdditiveContainer.generatedDataCollection](CAMAdditiveContainer_generatedDataCollection.htm), [CAMFolder.generatedDataCollection](CAMFolder_generatedDataCollection.htm), [CAMHoleRecognition.generatedDataCollection](CAMHoleRecognition_generatedDataCollection.htm), [CAMPattern.generatedDataCollection](CAMPattern_generatedDataCollection.htm), [NCProgram.generatedDataCollection](NCProgram_generatedDataCollection.htm), [Operation.generatedDataCollection](Operation_generatedDataCollection.htm), [OperationBase.generatedDataCollection](OperationBase_generatedDataCollection.htm), [Setup.generatedDataCollection](Setup_generatedDataCollection.htm)

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