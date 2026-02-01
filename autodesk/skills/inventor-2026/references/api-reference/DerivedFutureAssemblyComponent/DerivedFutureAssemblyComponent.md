# DerivedFutureAssemblyComponent Object

Derived from: [ReferenceComponent](../ReferenceComponent/ReferenceComponent.md) Object

## Description

The DerivedFutureAssemblyComponent object represents a specific derived future assembly instance.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [BreakLinkToFile](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_BreakLinkToFile.md) | Method that breaks the connection of the derived component with the part or assembly from which it was created. When the link is broken the ReferencedFile property will return Nothing. |
| [Delete](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_Delete.md) | Method that deletes the ReferenceComponent. |
| [GetReferenceKey](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Definition](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_Definition.md) | Read-write property that returns the derived future assembly definition that defines the current state of the derived future assembly.   The state of the derived future assembly can be changed by modifying the values of the returned descriptor and assigning it back to the derived future assembly using the DerivedFutureAssemblyDefinition property. The part will be updated as a result of the assignment. Note: Definition property will return Nothing if the link to the base assembly is broken or if the link to the base assembly could not be resolved. |
| [HealthStatus](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsEmbedded](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_IsEmbedded.md) | Property that returns whether the reference component refers to an embedded document or a linked document. |
| [LinkedToFile](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_LinkedToFile.md) | Property that returns whether the derived component is still linked to the base part or assembly document. If True, the link still exists. If False, the link has been broken and the ReferencedFile property will return Nothing. |
| [Name](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_Name.md) | Property that returns the component's name. |
| [Parent](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_Parent.md) | Property that returns the parent object. |
| [ReferencedDocumentDescriptor](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_ReferencedDocumentDescriptor.md) | Property that returns the DocumentDescriptor object. |
| [ReferenceFeatures](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_ReferenceFeatures.md) | Read-only property that returns the collection containing the ReferenceFeatures that were created as a result of the derived component. |
| [SuppressAll](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_SuppressAll.md) | Read-write property that gets and sets the suppress state for all of the Reference features created by this derived assembly component. |
| [SuppressLinkToFile](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_SuppressLinkToFile.md) | Read-write property that suppresses or unsuppresses the link to the base assembly. |
| [Type](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DerivedFutureAssemblyComponentProxy.NativeObject](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_NativeObject.md), [DerivedFutureAssemblyComponents.Add](../DerivedFutureAssemblyComponents/DerivedFutureAssemblyComponents_Add.md), [DerivedFutureAssemblyComponents.Item](../DerivedFutureAssemblyComponents/DerivedFutureAssemblyComponents_Item.md)

## Derived Classes

[DerivedFutureAssemblyComponentProxy](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy.md)

## Version

Introduced in version 2018
