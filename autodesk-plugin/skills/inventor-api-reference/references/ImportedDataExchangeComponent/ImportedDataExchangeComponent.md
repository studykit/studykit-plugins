# ImportedDataExchangeComponent Object

Derived from: [ImportedComponent](../ImportedComponent/ImportedComponent.md) Object

## Description

ImportedDataExchangeComponent Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [Update](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_Update.md) | Updates the component from the exchange if there is update available. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Definition](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_Definition.md) | Read-write property that gets and sets the ImportedComponentDefinition which defines the various inputs that were used to create the imported component. |
| [HealthStatus](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_Name.md) | Property that returns the component's name. |
| [Parent](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SuppressLinkToFile](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_SuppressLinkToFile.md) | Read-write property that gets and sets whether to suppress the connection of the imported component with the file from which it was created. |
| [Type](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Urn](../ImportedDataExchangeComponent/ImportedDataExchangeComponent_Urn.md) | Read-only property that returns the DataExchange urn. |

## Accessed From

[ImportedDataExchangeComponentProxy.NativeObject](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy_NativeObject.md)

## Derived Classes

[ImportedDataExchangeComponentProxy](../ImportedDataExchangeComponentProxy/ImportedDataExchangeComponentProxy.md)

## Version

Introduced in version 2023
