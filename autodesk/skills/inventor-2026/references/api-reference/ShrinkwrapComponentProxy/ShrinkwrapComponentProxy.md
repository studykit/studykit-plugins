# ShrinkwrapComponentProxy Object

Derived from: [ShrinkwrapComponent](../ShrinkwrapComponent/ShrinkwrapComponent.md) Object

## Description

Shrinkwrap Component Proxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_Definition.md) | Gets or Sets ShrinkwrapDefinition that defines the current state of this shrinkwrap component. |
| [HealthStatus](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_Name.md) | Property that returns the component's name. |
| [NativeObject](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [ReferenceFeatures](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_ReferenceFeatures.md) | Gets the ReferenceFeature objects that were created as a result of this shrinkwrap. |
| [SuppressLinkToFile](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_SuppressLinkToFile.md) | Gets and Sets a Boolean flag indicating whether the link to the assembly file is suppressed. |
| [Type](../ShrinkwrapComponentProxy/ShrinkwrapComponentProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2018
