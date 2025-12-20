# WeldsComponentDefinition Object

Derived from: [ComponentDefinition](../ComponentDefinition/ComponentDefinition.md) Object

## Description

The WeldsComponentDefinition object derives from the PartComponentDefinition object. It adds weld-specific behavior to the PartComponentDefinition.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [FindUsingPoint](../WeldsComponentDefinition/WeldsComponentDefinition_FindUsingPoint.md) | Method that finds all the entities of the specified type at the specified location. |
| [FindUsingVector](../WeldsComponentDefinition/WeldsComponentDefinition_FindUsingVector.md) | Method that finds all the entities of the specified type along the specified vector using either a cylinder or cone that to define the tolerance within the defined vector. |
| [GetUnusedGeometries](../WeldsComponentDefinition/WeldsComponentDefinition_GetUnusedGeometries.md) | Method that gets the unused sketches and work features. |
| [PurgeUnusedGeometries](../WeldsComponentDefinition/WeldsComponentDefinition_PurgeUnusedGeometries.md) | Method that purges unused sketches and work features. |
| [RepositionObject](../WeldsComponentDefinition/WeldsComponentDefinition_RepositionObject.md) | Method that repositions the specifies object(s) to the new position within the collection of the object in the document. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../WeldsComponentDefinition/WeldsComponentDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../WeldsComponentDefinition/WeldsComponentDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BOMQuantity](../WeldsComponentDefinition/WeldsComponentDefinition_BOMQuantity.md) | Property that returns the BOMQuantity object. |
| [BOMStructure](../WeldsComponentDefinition/WeldsComponentDefinition_BOMStructure.md) | Gets and sets how the component is used/viewed in a BOM. |
| [ClientGraphicsCollection](../WeldsComponentDefinition/WeldsComponentDefinition_ClientGraphicsCollection.md) | Property that returns the ClientGraphicsCollection object. |
| [DataIO](../WeldsComponentDefinition/WeldsComponentDefinition_DataIO.md) | Gets the object that directly deals with I/O to and from a storage-medium, including Streams(IStream). |
| [Document](../WeldsComponentDefinition/WeldsComponentDefinition_Document.md) | Property that returns the containing Document object. |
| [ModelGeometryVersion](../WeldsComponentDefinition/WeldsComponentDefinition_ModelGeometryVersion.md) | Property that returns a string that can be used to determine if the document has been modified. This version string is changed every time the assembly is modified. By saving a previous version string, you can compare the current version string to see if the assembly has been modified. |
| [Occurrences](../WeldsComponentDefinition/WeldsComponentDefinition_Occurrences.md) | Property that returns the collection object. |
| [OrientedMinimumRangeBox](../WeldsComponentDefinition/WeldsComponentDefinition_OrientedMinimumRangeBox.md) | Read-only property that returns the oriented minimum range box for this object. |
| [PreciseRangeBox](../WeldsComponentDefinition/WeldsComponentDefinition_PreciseRangeBox.md) | Gets a bounding box that tightly encloses all the solid and surface bodies under the ComponentDefinition. |
| [RangeBox](../WeldsComponentDefinition/WeldsComponentDefinition_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [SurfaceBodies](../WeldsComponentDefinition/WeldsComponentDefinition_SurfaceBodies.md) | Property that returns all of the *result* SurfaceBody objects contained within this ComponentDefinition. |
| [Type](../WeldsComponentDefinition/WeldsComponentDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[WeldmentComponentDefinition.WeldsComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition_WeldsComponentDefinition.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |