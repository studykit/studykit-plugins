# DerivedAliasComponentProxy Object

Derived from: [DerivedAliasComponent](../DerivedAliasComponent/DerivedAliasComponent.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [HealthStatus](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_Name.md) | Property that returns the component's name. |
| [NativeObject](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_Parent.md) | Property that returns the parent object. |
| [ReferencedAliasFullFilename](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_ReferencedAliasFullFilename.md) | Read-only property that returns the full filename of the derived Alias file. |
| [ReferencedDocumentDescriptor](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [ResultFeatures](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_ResultFeatures.md) | Property that returns the list of NonParametricBaseFeature objects that were created as a result of deriving this Alias file. |
| [Type](../DerivedAliasComponentProxy/DerivedAliasComponentProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |