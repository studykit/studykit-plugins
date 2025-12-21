# Parameters Object

## Description

Provides access to the objects associated with the object the collection was obtained from. Using the properties supported by the collection you can access the all of the parameters as a set or by type.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ExportToXML](../Parameters/Parameters_ExportToXML.md) | Exports parameters to XML file. |
| [GetValueFromExpression](../Parameters/Parameters_GetValueFromExpression.md) | Method that evaluates the input expression using the units specified and returns a value in database units. |
| [ImportFromXML](../Parameters/Parameters_ImportFromXML.md) | Imports parameters from XML file. |
| [IsExpressionValid](../Parameters/Parameters_IsExpressionValid.md) | Returns whether the input expression is valid or not. |
| [SetAllToMax](../Parameters/Parameters_SetAllToMax.md) | Method that sets the values of all parameters to be the maximum value as defined by the parameter's tolerance. |
| [SetAllToMedian](../Parameters/Parameters_SetAllToMedian.md) | Sets the values of all parameters to be the median value as defined by the parameter's tolerance. |
| [SetAllToMin](../Parameters/Parameters_SetAllToMin.md) | Method that sets the values of all parameters to be the minimum value as defined by the parameter's tolerance. |
| [SetAllToNominal](../Parameters/Parameters_SetAllToNominal.md) | Method that sets the values of all parameters to be the nominal value as defined by the parameter's tolerance. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AngularDimensionPrecision](../Parameters/Parameters_AngularDimensionPrecision.md) | Gets/Sets the precision for angular dimensions in this document. |
| [AngularStandardTolerance](../Parameters/Parameters_AngularStandardTolerance.md) | Gets/Sets the standard tolerance for angular dimensions in this document. |
| [Count](../Parameters/Parameters_Count.md) | Property that returns the number of items in this collection. |
| [CustomParameterGroups](../Parameters/Parameters_CustomParameterGroups.md) | Property that returns the CustomParameterGroups collection object. |
| [DerivedParameterTables](../Parameters/Parameters_DerivedParameterTables.md) | Property that returns the DerivedParameterTables collection object. |
| [DimensionDisplayType](../Parameters/Parameters_DimensionDisplayType.md) | Gets/Sets the dimension display type for dimensions in this document. |
| [DisplayParameterAsExpression](../Parameters/Parameters_DisplayParameterAsExpression.md) | Gets and sets whether parameters are displayed as values or expressions in edit boxes when a dimension or a feature is edited. |
| [ExportStandardTolerances](../Parameters/Parameters_ExportStandardTolerances.md) | Gets and sets whether to export dimensions to drawings using the standard tolerance values. |
| [FinishParameters](../Parameters/Parameters_FinishParameters.md) | Gets the collection of Finish Feature parameters. |
| [Item](../Parameters/Parameters_Item.md) | Returns the specified Parameter object from the collection. This is the default property of the Parameters collection object. |
| [LinearDimensionPrecision](../Parameters/Parameters_LinearDimensionPrecision.md) | Gets/Sets the precision for linear dimensions in this document. |
| [LinearStandardTolerance](../Parameters/Parameters_LinearStandardTolerance.md) | Gets/Sets the standard tolerance for linear dimensions in this document. |
| [ModelParameters](../Parameters/Parameters_ModelParameters.md) | Property that returns the ModelParameters collection object. |
| [ParameterTables](../Parameters/Parameters_ParameterTables.md) | Property that returns the ParameterTables collection object. |
| [ReferenceParameters](../Parameters/Parameters_ReferenceParameters.md) | Property that returns the ReferenceParameters collection object. |
| [Type](../Parameters/Parameters_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserParameters](../Parameters/Parameters_UserParameters.md) | Property that returns the UserParameters collection object. |
| [UseStandardTolerances](../Parameters/Parameters_UseStandardTolerances.md) | Gets/Sets the boolean flag indicating whether to use standard tolerances for dimensions in this document. |

## Accessed From

[AssemblyComponentDefinition.Parameters](../AssemblyComponentDefinition/AssemblyComponentDefinition_Parameters.md), [DrawingDocument.Parameters](../DrawingDocument/DrawingDocument_Parameters.md), [FlatPattern.Parameters](../FlatPattern/FlatPattern_Parameters.md), [PartComponentDefinition.Parameters](../PartComponentDefinition/PartComponentDefinition_Parameters.md), [SheetMetalComponentDefinition.Parameters](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Parameters.md), [WeldmentComponentDefinition.Parameters](../WeldmentComponentDefinition/WeldmentComponentDefinition_Parameters.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Selectively link paramaters](../../sample-programs/DerivedParameterTables_Add2_Sample.md) | This sample demonstrates the selective linking of parameters from another Inventor file. |
| [Display information about parameter tolerances.](../../sample-programs/DumpParmeterInfo_Sample.md) | Dumps out information to the Immediate window about tolerance information associated with parameters. A part document must be active when this is run. |
| [Create user parameters](../../sample-programs/ParameterCreateUser_Sample.md) | This sample demonstrates creating user parameters using an expression and a value. A part document must be open and it must not contain user parameters named "NewParam1" and "NewParam2". |
| [Model Parameters](../../sample-programs/Parameters_Sample.md) | This sample demonstrates the methods and properties supported by the Parameters object for model parameters. |
| [Set the value of a parameter](../../sample-programs/ParameterSetValue_Sample.md) | Sets the value of an existing parameter. A part must be open that contains a parameter named "Length". |
| [Table Parameters](../../sample-programs/ParameterTables_Sample.md) | This sample demonstrates how to access the Parameters object, and from it in turn the TableParameters collection that represents the collection of parameters that have been linked/embedded from an external spreadsheet. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |