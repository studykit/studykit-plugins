# DerivedAssemblyComponentProxy Object

Derived from: [DerivedAssemblyComponent](../DerivedAssemblyComponent/DerivedAssemblyComponent.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Replace](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_Replace.md) | Replaces current derived assembly component with another file. |
| [SetEndOfPart](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_Definition.md) | Gets or sets DerivedAssemblyDefinition that defines the current state of this derived assembly. |
| [HealthStatus](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_Name.md) | Property that returns the component's name. |
| [NativeObject](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [ReferenceFeatures](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_ReferenceFeatures.md) | Property that returns the collection containing the ReferenceFeatures that was created as a result of the derived component. |
| [SuppressAll](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_SuppressAll.md) | Property that gets and sets the suppress state for all of the Reference features created by this derived assembly component. |
| [SuppressLinkToFile](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_SuppressLinkToFile.md) | Gets and Sets a Boolean flag indicating whether the link to the assembly file is suppressed. |
| [Type](../DerivedAssemblyComponentProxy/DerivedAssemblyComponentProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2008
