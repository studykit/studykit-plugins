# ReferenceComponents Object

## Description

Provides access to all of the objects that are owned by a particular PartComponentDefinition and have an external file reference.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ReferenceComponents/ReferenceComponents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DerivedAliasComponents](../ReferenceComponents/ReferenceComponents_DerivedAliasComponents.md) | Property that returns the DerivedAliasComponents collection object. |
| [DerivedAssemblyComponents](../ReferenceComponents/ReferenceComponents_DerivedAssemblyComponents.md) | Property that returns the DerivedAssemblyComponent collection object. |
| [DerivedFutureAssemblyComponents](../ReferenceComponents/ReferenceComponents_DerivedFutureAssemblyComponents.md) | Gets the DerivedFutureAssemblyComponents collection object. |
| [DerivedFuturePartComponents](../ReferenceComponents/ReferenceComponents_DerivedFuturePartComponents.md) | Gets the DerivedFuturePartComponents collection object. |
| [DerivedPartComponents](../ReferenceComponents/ReferenceComponents_DerivedPartComponents.md) | Property that returns the DerivedPartComponents collection object. |
| [iFeatureTemplateDescriptors](../ReferenceComponents/ReferenceComponents_iFeatureTemplateDescriptors.md) | Property that returns the iFeatureTemplateDescriptors collection object. This collection provides access to existing iFeatureTemplateDescriptor objects. Note: iFeatureTemplateDescriptors was previously known as iFeatureDescriptors and were accessed through the DerivativeDescriptors collection. The DerivativeDescriptors collection has been removed and is now obsolete. |
| [ImportedComponents](../ReferenceComponents/ReferenceComponents_ImportedComponents.md) | Read-only property that returns the ImportedComponents collection object. This collection provides access to existing ImportedComponent objects and provides functionality to create new ImportedComponent objects. |
| [ShrinkwrapComponents](../ReferenceComponents/ReferenceComponents_ShrinkwrapComponents.md) | Gets the ShrinkwrapComponents collection object. |
| [Type](../ReferenceComponents/ReferenceComponents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PartComponentDefinition.ReferenceComponents](../PartComponentDefinition/PartComponentDefinition_ReferenceComponents.md), [SheetMetalComponentDefinition.ReferenceComponents](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ReferenceComponents.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [ImportedDWGComponent Creation](../../sample-programs/ImportedDWGComponentCreation_Sample.md) | This sample demonstrates how to create an imported DWG component into Inventor part document, and project the DWG entities onto Inventor planar sketch. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |