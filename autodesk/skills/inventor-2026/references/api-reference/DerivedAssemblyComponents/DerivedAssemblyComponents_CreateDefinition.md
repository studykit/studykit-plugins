# DerivedAssemblyComponents.CreateDefinition Method

Parent Object: [DerivedAssemblyComponents](../DerivedAssemblyComponents/DerivedAssemblyComponents.md)

## Description

Method that creates a new Definition. The returned definition provides access to all of the items in the document that can be derived.

## Remarks

Using this object you define which of these items will be derived when the derived component is created. When a DerivedAssemblyDefinition is initially created it is set so all available entities will be included in the derived component.

## Syntax

DerivedAssemblyComponents.**CreateDefinition**( ***FullDocumentName*** As String ) As [DerivedAssemblyDefinition](../DerivedAssemblyDefinition/DerivedAssemblyDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullDocumentName | String | String that specifies the full document name of the assembly document to create the definition for. If only the FullFileName is specified, the master document within the assembly file is opened. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Shrink wrap substitute in assembly](../../sample-programs/Shrinkwrap_Sample.md) | The following sample demonstrates the creation of a shrinkwrap substitute within an assembly. |

## Version

Introduced in version 5.3
