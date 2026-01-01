# ManufacturingModel Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/ManufacturingModels/ManufacturingModel.h>

## Description

Represents a ManufacturingModel within a CAM design. A Manufacturing Model is a derive of the Design scene, which can be augmented without any effects of the original Design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [activate](ManufacturingModel_activate.htm) | Makes the ManufacturingModel the active edit target in the user interface. This is the same as enabling the radio button next to the occurrence in the browser. |
| [classType](ManufacturingModel_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](ManufacturingModel_deleteMe.htm) | Deletes this ManufacturingModel. If this is part of a setup, the reference to this will be lost. The deletion makes that reference invalid. |
| [duplicate](ManufacturingModel_duplicate.htm) | Creates and returns a copy of the ManufacturingModel, within its parent collection. The newly created ManufacturingModel will have a new unique name assigned. |
| [syncManufacturingModel](ManufacturingModel_syncManufacturingModel.htm) | Checks whether changes to the original design have been made. If so, the given manufacturing model is synchronized with its source. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [id](ManufacturingModel_id.htm) | Gets the unique identifier of the ManufacturingModel within the document. |
| [isActive](ManufacturingModel_isActive.htm) | Gets whether this ManufacturingModel is active in the user interface. This is the same as checking the state of the radio button next to the ManufacturingModel in the browser. To activate the ManufacturingModel use the Activate method. |
| [isValid](ManufacturingModel_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](ManufacturingModel_name.htm) | Gets or sets the display name of the ManufacturingModel. This is the name that will be shown in the browser and other locations. |
| [objectType](ManufacturingModel_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [occurrence](ManufacturingModel_occurrence.htm) | Returns the occurrence for that ManufacturingModel. |

## Accessed From

[ManufacturingModel.duplicate](ManufacturingModel_duplicate.htm), [ManufacturingModels.add](ManufacturingModels_add.htm), [ManufacturingModels.item](ManufacturingModels_item.htm), [ManufacturingModels.itemById](ManufacturingModels_itemById.htm), [ManufacturingModels.itemByName](ManufacturingModels_itemByName.htm)

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