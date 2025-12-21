# ImportedRVTComponent Object

Derived from: [ImportedComponent](../ImportedComponent/ImportedComponent.md) Object

## Description

ImportedRVTComponent Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../ImportedRVTComponent/ImportedRVTComponent_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../ImportedRVTComponent/ImportedRVTComponent_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../ImportedRVTComponent/ImportedRVTComponent_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../ImportedRVTComponent/ImportedRVTComponent_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ImportedRVTComponent/ImportedRVTComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ImportedRVTComponent/ImportedRVTComponent_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Definition](../ImportedRVTComponent/ImportedRVTComponent_Definition.md) | Read-write property that gets and sets the ImportedComponentDefinition which defines the various inputs that were used to create the imported component. |
| [HealthStatus](../ImportedRVTComponent/ImportedRVTComponent_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../ImportedRVTComponent/ImportedRVTComponent_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../ImportedRVTComponent/ImportedRVTComponent_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../ImportedRVTComponent/ImportedRVTComponent_Name.md) | Property that returns the component's name. |
| [Parent](../ImportedRVTComponent/ImportedRVTComponent_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../ImportedRVTComponent/ImportedRVTComponent_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SuppressLinkToFile](../ImportedRVTComponent/ImportedRVTComponent_SuppressLinkToFile.md) | Read-write property that gets and sets whether to suppress the connection of the imported component with the file from which it was created. |
| [Type](../ImportedRVTComponent/ImportedRVTComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ImportedRVTComponentProxy.NativeObject](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_NativeObject.md)

## Derived Classes

[ImportedRVTComponentProxy](../ImportedRVTComponentProxy/ImportedRVTComponentProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Import Revit data into Inventor](../../sample-programs/ImportRevitIntoInventor_Sample.md) | The samples demonstrate how to import Revit data(.rvt) into Inventor part and assembly documents. |

## Version

Introduced in version 2021
