# ImportedRVTComponentProxy Object

Derived from: [ImportedRVTComponent](../ImportedRVTComponent/ImportedRVTComponent.md) Object

## Description

ImportedRVTComponentProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_ContainingOccurrence.md) | Get the component occurrence context through which the native object is being seen through. |
| [Definition](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_Definition.md) | Read-write property that gets and sets the ImportedComponentDefinition which defines the various inputs that were used to create the imported component. |
| [HealthStatus](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_Name.md) | Property that returns the component's name. |
| [NativeObject](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_NativeObject.md) | Get the object in the context of the definition instead of the containing assembly. |
| [Parent](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SuppressLinkToFile](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_SuppressLinkToFile.md) | Read-write property that gets and sets whether to suppress the connection of the imported component with the file from which it was created. |
| [Type](../ImportedRVTComponentProxy/ImportedRVTComponentProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2021
