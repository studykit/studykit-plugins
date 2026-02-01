# VirtualComponentDefinition Object

Derived from: [ComponentDefinition](../ComponentDefinition/ComponentDefinition.md) Object

## Description

This object derives from the ComponentDefinition object. It represents a ComponentDefinition that exists solely for the BOM.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [FindUsingPoint](../VirtualComponentDefinition/VirtualComponentDefinition_FindUsingPoint.md) | Method that finds all the entities of the specified type at the specified location. |
| [FindUsingVector](../VirtualComponentDefinition/VirtualComponentDefinition_FindUsingVector.md) | Method that finds all the entities of the specified type along the specified vector using either a cylinder or cone that to define the tolerance within the defined vector. |
| [GetUnusedGeometries](../VirtualComponentDefinition/VirtualComponentDefinition_GetUnusedGeometries.md) | Method that gets the unused sketches and work features. |
| [PurgeUnusedGeometries](../VirtualComponentDefinition/VirtualComponentDefinition_PurgeUnusedGeometries.md) | Method that purges unused sketches and work features. |
| [RepositionObject](../VirtualComponentDefinition/VirtualComponentDefinition_RepositionObject.md) | Method that repositions the specifies object(s) to the new position within the collection of the object in the document. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveMaterial](../VirtualComponentDefinition/VirtualComponentDefinition_ActiveMaterial.md) | Gets and sets the material for the VirtualComponentDefinition. |
| [Application](../VirtualComponentDefinition/VirtualComponentDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../VirtualComponentDefinition/VirtualComponentDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BOMQuantity](../VirtualComponentDefinition/VirtualComponentDefinition_BOMQuantity.md) | Property that returns the BOMQuantity object. |
| [BOMStructure](../VirtualComponentDefinition/VirtualComponentDefinition_BOMStructure.md) | Gets and sets how the component is used/viewed in a BOM. |
| [ClientGraphicsCollection](../VirtualComponentDefinition/VirtualComponentDefinition_ClientGraphicsCollection.md) | Property that returns the ClientGraphicsCollection object. |
| [DataIO](../VirtualComponentDefinition/VirtualComponentDefinition_DataIO.md) | Gets the object that directly deals with I/O to and from a storage-medium, including Streams(IStream). |
| [DisplayName](../VirtualComponentDefinition/VirtualComponentDefinition_DisplayName.md) | Gets and sets the name of the virtual component. |
| [Document](../VirtualComponentDefinition/VirtualComponentDefinition_Document.md) | Property that returns the containing Document object. |
| [ModelGeometryVersion](../VirtualComponentDefinition/VirtualComponentDefinition_ModelGeometryVersion.md) | Property that returns a string that can be used to determine if the document has been modified. This version string is changed every time the assembly is modified. By saving a previous version string, you can compare the current version string to see if the assembly has been modified. |
| [Occurrences](../VirtualComponentDefinition/VirtualComponentDefinition_Occurrences.md) | Property that returns the collection object. |
| [OrientedMinimumRangeBox](../VirtualComponentDefinition/VirtualComponentDefinition_OrientedMinimumRangeBox.md) | Read-only property that returns the oriented minimum range box for this object. |
| [PreciseRangeBox](../VirtualComponentDefinition/VirtualComponentDefinition_PreciseRangeBox.md) | Gets a bounding box that tightly encloses all the solid and surface bodies under the ComponentDefinition. |
| [PropertySets](../VirtualComponentDefinition/VirtualComponentDefinition_PropertySets.md) | Property that gets the PropertySets object associated with the virtual component. |
| [RangeBox](../VirtualComponentDefinition/VirtualComponentDefinition_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [SurfaceBodies](../VirtualComponentDefinition/VirtualComponentDefinition_SurfaceBodies.md) | Property that returns all of the *result* SurfaceBody objects contained within this ComponentDefinition. |
| [Type](../VirtualComponentDefinition/VirtualComponentDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |

## Version

Introduced in version 10
