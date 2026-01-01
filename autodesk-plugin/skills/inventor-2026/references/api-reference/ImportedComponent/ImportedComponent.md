# ImportedComponent Object

Derived from: [ReferenceComponent](../ReferenceComponent/ReferenceComponent.md) Object

## Description

ImportedComponent Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../ImportedComponent/ImportedComponent_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../ImportedComponent/ImportedComponent_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../ImportedComponent/ImportedComponent_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../ImportedComponent/ImportedComponent_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ImportedComponent/ImportedComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ImportedComponent/ImportedComponent_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Definition](../ImportedComponent/ImportedComponent_Definition.md) | Read-write property that gets and sets the ImportedComponentDefinition which defines the various inputs that were used to create the imported component. |
| [HealthStatus](../ImportedComponent/ImportedComponent_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../ImportedComponent/ImportedComponent_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../ImportedComponent/ImportedComponent_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../ImportedComponent/ImportedComponent_Name.md) | Property that returns the component's name. |
| [Parent](../ImportedComponent/ImportedComponent_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../ImportedComponent/ImportedComponent_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [SuppressLinkToFile](../ImportedComponent/ImportedComponent_SuppressLinkToFile.md) | Read-write property that gets and sets whether to suppress the connection of the imported component with the file from which it was created. |
| [Type](../ImportedComponent/ImportedComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ComponentOccurrence.ImportedComponent](../ComponentOccurrence/ComponentOccurrence_ImportedComponent.md), [ComponentOccurrenceProxy.ImportedComponent](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_ImportedComponent.md), [ImportedComponentDefinition.Parent](../ImportedComponentDefinition/ImportedComponentDefinition_Parent.md), [ImportedComponentProxy.NativeObject](../ImportedComponentProxy/ImportedComponentProxy_NativeObject.md), [ImportedComponents.Add](../ImportedComponents/ImportedComponents_Add.md), [ImportedComponents.Item](../ImportedComponents/ImportedComponents_Item.md), [ImportedDataExchangeComponentDefinition.Parent](../ImportedDataExchangeComponentDefinition/ImportedDataExchangeComponentDefinition_Parent.md), [ImportedDWGComponentDefinition.Parent](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_Parent.md), [ImportedGenericComponentDefinition.Parent](../ImportedGenericComponentDefinition/ImportedGenericComponentDefinition_Parent.md), [ImportedRVTComponentDefinition.Parent](../ImportedRVTComponentDefinition/ImportedRVTComponentDefinition_Parent.md)

## Derived Classes

[ImportedDataExchangeComponent](../ImportedDataExchangeComponent/ImportedDataExchangeComponent.md), [ImportedDWGComponent](../ImportedDWGComponent/ImportedDWGComponent.md), [ImportedGenericComponent](../ImportedGenericComponent/ImportedGenericComponent.md), [ImportedRVTComponent](../ImportedRVTComponent/ImportedRVTComponent.md)

## Version

Introduced in version 2016
