# DerivedAliasComponent Object

Derived from: [ReferenceComponent](../ReferenceComponent/ReferenceComponent.md) Object

## Description

The DerivedAliasComponent object represents a specific derived Alias instance.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../DerivedAliasComponent/DerivedAliasComponent_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../DerivedAliasComponent/DerivedAliasComponent_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../DerivedAliasComponent/DerivedAliasComponent_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../DerivedAliasComponent/DerivedAliasComponent_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedAliasComponent/DerivedAliasComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DerivedAliasComponent/DerivedAliasComponent_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [HealthStatus](../DerivedAliasComponent/DerivedAliasComponent_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../DerivedAliasComponent/DerivedAliasComponent_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../DerivedAliasComponent/DerivedAliasComponent_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../DerivedAliasComponent/DerivedAliasComponent_Name.md) | Property that returns the component's name. |
| [Parent](../DerivedAliasComponent/DerivedAliasComponent_Parent.md) | Property that returns the parent object. |
| [ReferencedAliasFullFilename](../DerivedAliasComponent/DerivedAliasComponent_ReferencedAliasFullFilename.md) | Read-only property that returns the full filename of the derived Alias file. |
| [ReferencedDocumentDescriptor](../DerivedAliasComponent/DerivedAliasComponent_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [ResultFeatures](../DerivedAliasComponent/DerivedAliasComponent_ResultFeatures.md) | Property that returns the list of NonParametricBaseFeature objects that were created as a result of deriving this Alias file. |
| [Type](../DerivedAliasComponent/DerivedAliasComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DerivedAliasComponentProxy.NativeObject](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_NativeObject.md), [DerivedAliasComponents.Item](../DerivedAliasComponents/DerivedAliasComponents_Item.md)

## Derived Classes

[DerivedAliasComponentProxy](../DerivedAliasComponentProxy/DerivedAliasComponentProxy.md)

## Version

Introduced in version 2010
