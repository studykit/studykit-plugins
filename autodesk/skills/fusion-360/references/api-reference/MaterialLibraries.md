# MaterialLibraries Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Materials/MaterialLibraries.h>

## Description

The MaterialLibraries collection object provides access to currently loaded Material and Appearance libraries

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MaterialLibraries_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](MaterialLibraries_item.htm) | Method that returns the specified Material Library using an index into the collection. |
| [itemById](MaterialLibraries_itemById.htm) | Returns the Material Library at the specified ID. |
| [itemByName](MaterialLibraries_itemByName.htm) | Returns the specified Material Library using the name as seen in the user interface. |
| [load](MaterialLibraries_load.htm) | Loads the specified existing local material library. Fusion remembers which libraries have been loaded from one session to the next so you should check to see if the local library is already loaded or not before loading it again. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](MaterialLibraries_count.htm) | The number of Material Libraries in the collection. |
| [isValid](MaterialLibraries_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](MaterialLibraries_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Application.materialLibraries](Application_materialLibraries.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Avoid Machine Surface Settings API Sample](AvoidMachineSurfaceSettings_Sample.htm) | This sample script demonstrates how to use Machine/Avoid/Gouge/Fixture functionality.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a curved surface with a through slot, a countersunk hole and a raised, circular and filleted upstand from the surface. The model is supported by two rectangular blocks, themselves mounted on a fixture plate. A setup is included with a single operation running a 3-axis diagonal raster over the model, supports and fixture. The operation machines the fixture, the supporting blocks, the upper surface of the upstand and the area within the slot and hole, something we would like to avoid.  The script duplicates the original operation and then proceeds to create a series of MachineAvoidGroups. These are labelled as either Machine in the case of 2 cap surfaces for the slot and hole, Fixture for the fixture plate, Gouge for the supporting blocks and Avoid for the top face of the upstand. Additionally, both AxialOffset and RadialOffset can be specified for the Machine, Avoid and Fixture passes. |
| [Create Engravings Selection Sets API Sample](CreateEngravingsSelectionSets_Sample.htm) | This sample script demonstrates how to find and machine engravings in the Z+ direction using pocket recognition.  The script will first open an example model via its URN. Using pocket recognition, it will identify pockets that may be engravings based on their dimensions.  We assume here that an engraving pocket is:  * Made with a flat bottom face and no fillet. * A closed pocket. * Have a Z height less than 2 mm   We demonstrate creating selection sets in both design and manufacture workspaces and use one of the selection sets as an operation geometry selection input to generate an engraving operation.  The engraving toolpath can be seen by expanding the setup and selecting the operation. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |