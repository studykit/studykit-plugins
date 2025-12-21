# ImportedDataExchangeComponentProxy Object

Derived from: [ImportedDataExchangeComponent](../ImportedDataExchangeComponent/ImportedDataExchangeComponent.md) Object

## Description

ImportedDataExchangeComponentProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [Update](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_Update.md) | Updates the component from the exchange if there is update available. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_ContainingOccurrence.md) | Get the component occurrence context through which the native object is being seen through. |
| [Definition](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_Definition.md) | Read-write property that gets and sets the ImportedComponentDefinition which defines the various inputs that were used to create the imported component. |
| [HealthStatus](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_Name.md) | Property that returns the component's name. |
| [NativeObject](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_NativeObject.md) | Get the object in the context of the definition instead of the containing assembly. |
| [Parent](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SuppressLinkToFile](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_SuppressLinkToFile.md) | Read-write property that gets and sets whether to suppress the connection of the imported component with the file from which it was created. |
| [Type](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Urn](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_Urn.md) | Read-only property that returns the DataExchange urn. |

## Version

Introduced in version 2023
