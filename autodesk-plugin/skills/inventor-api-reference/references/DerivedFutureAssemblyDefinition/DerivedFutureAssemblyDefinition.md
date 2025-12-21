# DerivedFutureAssemblyDefinition Object

## Description

The DerivedFutureAssemblyDefinition object is used to describe which parts in an assembly will be used during the creation of the DerivedAssemblyComponent. It is also used when querying and editing an existing derived assembly.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveDesignViewRepresentation](../DerivedFutureAssemblyDefinition/DerivedFutureAssemblyDefinition_ActiveDesignViewRepresentation.md) | Read-write property that gets and sets the name of the active Design View Representation for the derived future assembly. An empty string indicates the Master design view is used. The IsAssociativeDesignView property indicates if an associate link to the design view is created or not. |
| [ActivePositionalRepresentation](../DerivedFutureAssemblyDefinition/DerivedFutureAssemblyDefinition_ActivePositionalRepresentation.md) | Read-write property that gets and sets the name of the active Positional Representation for the derived future assembly. |
| [Application](../DerivedFutureAssemblyDefinition/DerivedFutureAssemblyDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [FullFileName](../DerivedFutureAssemblyDefinition/DerivedFutureAssemblyDefinition_FullFileName.md) | Read-only property that gets the full filename of the derived document. |
| [IsAssociativeDesignView](../DerivedFutureAssemblyDefinition/DerivedFutureAssemblyDefinition_IsAssociativeDesignView.md) | Read-write property that gets and sets if there is an associative link to the specified design view. When creating a new derived future assembly, setting this property to True (which is the default) will create a derivation that is associative to the design view. This can only be set to True when a design view other than the master design view is specified. |
| [Occurrences](../DerivedFutureAssemblyDefinition/DerivedFutureAssemblyDefinition_Occurrences.md) | Read-only property that returns the derived assemblies. |
| [Type](../DerivedFutureAssemblyDefinition/DerivedFutureAssemblyDefinition_Type.md) | Read-only property returning kDerivedFutureAssemblyDefinitionObject indicating the type of object. |

## Accessed From

[DerivedFutureAssemblyComponent.Definition](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent_Definition.md), [DerivedFutureAssemblyComponentProxy.Definition](../DerivedFutureAssemblyComponentProxy/DerivedFutureAssemblyComponentProxy_Definition.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |