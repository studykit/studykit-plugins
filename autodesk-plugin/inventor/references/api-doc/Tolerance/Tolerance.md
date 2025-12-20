# Tolerance Object

## Description

The Tolerance object represents information about tolerance.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [SetToBasic](../Tolerance/Tolerance_SetToBasic.md) | Sets the type of this tolerance to be a basic type of tolerance (only valid for drawing dimensions). |
| [SetToDefault](../Tolerance/Tolerance_SetToDefault.md) | Method that sets the tolerance to the default value. |
| [SetToDeviation](../Tolerance/Tolerance_SetToDeviation.md) | Method that sets the type of this tolerance to be a deviation tolerance. |
| [SetToFits](../Tolerance/Tolerance_SetToFits.md) | Method that sets the type of this tolerance to be a fits tolerance. |
| [SetToLimits](../Tolerance/Tolerance_SetToLimits.md) | Method that sets the type of this tolerance to be a limits tolerance. |
| [SetToMax](../Tolerance/Tolerance_SetToMax.md) | Sets the type of this tolerance to be a MAX type of tolerance. |
| [SetToMin](../Tolerance/Tolerance_SetToMin.md) | Sets the type of this tolerance to be a MIN type of tolerance. |
| [SetToReference](../Tolerance/Tolerance_SetToReference.md) | Sets the type of this tolerance to be a reference type of tolerance (only valid for drawing dimensions). |
| [SetToSymmetric](../Tolerance/Tolerance_SetToSymmetric.md) | Method that sets the type of this tolerance to be a symmetric tolerance. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [HoleTolerance](../Tolerance/Tolerance_HoleTolerance.md) | Property that returns a string specifying the hole tolerance. |
| [Lower](../Tolerance/Tolerance_Lower.md) | Property that returns the lower variation from the nominal value in database units. |
| [Parent](../Tolerance/Tolerance_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [ShaftTolerance](../Tolerance/Tolerance_ShaftTolerance.md) | Property that returns the shaft tolerance. |
| [ToleranceType](../Tolerance/Tolerance_ToleranceType.md) | Property that returns a constant specifying the tolerance type. |
| [Type](../Tolerance/Tolerance_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Upper](../Tolerance/Tolerance_Upper.md) | Property that returns a constant specifying the upper variation from the nominal value in database units. |

## Accessed From

[AngularGeneralDimension.Tolerance](../AngularGeneralDimension/AngularGeneralDimension_Tolerance.md), [AngularModelDimensionDefinition.Tolerance](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_Tolerance.md), [DerivedParameter.Tolerance](../DerivedParameter/DerivedParameter_Tolerance.md), [DiameterGeneralDimension.Tolerance](../DiameterGeneralDimension/DiameterGeneralDimension_Tolerance.md), [DiameterModelDimensionDefinition.Tolerance](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_Tolerance.md), [DimensionStyle.Tolerance](../DimensionStyle/DimensionStyle_Tolerance.md), [DrawingDimension.Tolerance](../DrawingDimension/DrawingDimension_Tolerance.md), [FinishParameter.Tolerance](../FinishParameter/FinishParameter_Tolerance.md), [GeneralDimension.Tolerance](../GeneralDimension/GeneralDimension_Tolerance.md), [HoleThreadNote.Tolerance](../HoleThreadNote/HoleThreadNote_Tolerance.md), [LinearGeneralDimension.Tolerance](../LinearGeneralDimension/LinearGeneralDimension_Tolerance.md), [LinearModelDimensionDefinition.Tolerance](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_Tolerance.md), [MiniToolbarValueEditor.Tolerance](../MiniToolbarValueEditor/MiniToolbarValueEditor_Tolerance.md), [ModelDimensionDefinition.Tolerance](../ModelDimensionDefinition/ModelDimensionDefinition_Tolerance.md), [ModelHoleThreadNoteDefinition.GetHolePropertyTolerance](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_GetHolePropertyTolerance.md), [ModelParameter.Tolerance](../ModelParameter/ModelParameter_Tolerance.md), [OrdinateDimension.Tolerance](../OrdinateDimension/OrdinateDimension_Tolerance.md), [Parameter.Tolerance](../Parameter/Parameter_Tolerance.md), [RadiusGeneralDimension.Tolerance](../RadiusGeneralDimension/RadiusGeneralDimension_Tolerance.md), [RadiusModelDimensionDefinition.Tolerance](../RadiusModelDimensionDefinition/RadiusModelDimensionDefinition_Tolerance.md), [ReferenceParameter.Tolerance](../ReferenceParameter/ReferenceParameter_Tolerance.md), [TableParameter.Tolerance](../TableParameter/TableParameter_Tolerance.md), [UserParameter.Tolerance](../UserParameter/UserParameter_Tolerance.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Display information about parameter tolerances.](../../sample-programs/DumpParmeterInfo_Sample.md) | Dumps out information to the Immediate window about tolerance information associated with parameters. A part document must be active when this is run. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |