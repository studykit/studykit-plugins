# DerivedFutureAssemblyComponentProxy Object

Derived from: [DerivedFutureAssemblyComponent](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent.md) Object

## Description

DerivedFutureAssemblyComponentProxy object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_Definition.md) | Read-write property that returns the derived future assembly definition that defines the current state of the derived future assembly.   The state of the derived future assembly can be changed by modifying the values of the returned descriptor and assigning it back to the derived future assembly using the DerivedFutureAssemblyDefinition property. The part will be updated as a result of the assignment. Note: Definition property will return Nothing if the link to the base assembly is broken or if the link to the base assembly could not be resolved. |
| [HealthStatus](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_Name.md) | Property that returns the component's name. |
| [NativeObject](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parent](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [ReferenceFeatures](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_ReferenceFeatures.md) | Read-only property that returns the collection containing the ReferenceFeatures that were created as a result of the derived component. |
| [SuppressAll](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_SuppressAll.md) | Read-write property that gets and sets the suppress state for all of the Reference features created by this derived assembly component. |
| [SuppressLinkToFile](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_SuppressLinkToFile.md) | Read-write property that suppresses or unsuppresses the link to the base assembly. |
| [Type](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |