# LinearGeneralDimension Object

Derived from: [GeneralDimension](../GeneralDimension/GeneralDimension.md) Object

## Description

The LinearGeneralDimension object represents a linear general dimension placed on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CenterText](../LinearGeneralDimension/LinearGeneralDimension_CenterText.md) | Method that centers the dimension text on the dimension line. |
| [Delete](../LinearGeneralDimension/LinearGeneralDimension_Delete.md) | Method that deletes the DrawingDimension. |
| [GetInspectionDimensionData](../LinearGeneralDimension/LinearGeneralDimension_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [GetReferenceKey](../LinearGeneralDimension/LinearGeneralDimension_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [PromoteToSketch](../LinearGeneralDimension/LinearGeneralDimension_PromoteToSketch.md) | Method that copies the dimension to the underlying sketch. This method only works for dimensions associated with a draft view. |
| [SetInspectionDimensionData](../LinearGeneralDimension/LinearGeneralDimension_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn't already. |
| [ShowAllExtensionLines](../LinearGeneralDimension/LinearGeneralDimension_ShowAllExtensionLines.md) | Method that un-hides all the extension lines associated with this dimension. If there are no hidden extension lines associated with this dimension, this method does nothing and returns a success. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AlignmentGeometry](../LinearGeneralDimension/LinearGeneralDimension_AlignmentGeometry.md) | Read-only property that returns the geometry that defines the direction the linear dimension aligns to. |
| [Application](../LinearGeneralDimension/LinearGeneralDimension_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrowheadsInside](../LinearGeneralDimension/LinearGeneralDimension_ArrowheadsInside.md) | Gets and sets the ArrowheadsInside setting. |
| [Attached](../LinearGeneralDimension/LinearGeneralDimension_Attached.md) | Indicates whether this dimension is attached to anything. If not, it is considered orphaned and can be removed. |
| [AttributeSets](../LinearGeneralDimension/LinearGeneralDimension_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BaselineDimensionSet](../LinearGeneralDimension/LinearGeneralDimension_BaselineDimensionSet.md) | Property that returns the BaselineDimensionSet that owns this dimension. |
| [ChainDimensionSet](../LinearGeneralDimension/LinearGeneralDimension_ChainDimensionSet.md) | Property that returns the ChainDimensionSet that owns this dimension. This property returns nothing if this dimension is not a chain dimension set member. This can be checked using the *IsChainSetMember* property. |
| [DimensionLine](../LinearGeneralDimension/LinearGeneralDimension_DimensionLine.md) | Property that returns the dimension line geometry of the dimension. |
| [DimensionType](../LinearGeneralDimension/LinearGeneralDimension_DimensionType.md) | Property that returns the dimension type. Possible values are kAlignedDimensionType, kHorizontalDimensionType, kVerticalDimensionType, kArcLengthDimensionType, kSymmetricDimensionType and kDiametricDimensionType. |
| [ExtensionLineOne](../LinearGeneralDimension/LinearGeneralDimension_ExtensionLineOne.md) | Property that returns the first extension line of the dimension. |
| [ExtensionLineOneVisible](../LinearGeneralDimension/LinearGeneralDimension_ExtensionLineOneVisible.md) | Gets and sets whether the first extension line is visible. |
| [ExtensionLineTwo](../LinearGeneralDimension/LinearGeneralDimension_ExtensionLineTwo.md) | Property that returns the second extension line of the dimension. |
| [ExtensionLineTwoVisible](../LinearGeneralDimension/LinearGeneralDimension_ExtensionLineTwoVisible.md) | Gets and sets whether the second extension line is visible. |
| [FirstArrowheadInside](../LinearGeneralDimension/LinearGeneralDimension_FirstArrowheadInside.md) | Read-write property that gets and sets whether the first arrowhead is inside or outside. |
| [FirstArrowheadType](../LinearGeneralDimension/LinearGeneralDimension_FirstArrowheadType.md) | Read-write property that gets and sets the type of the first arrowhead. |
| [FullDimensionLine](../LinearGeneralDimension/LinearGeneralDimension_FullDimensionLine.md) | Gets and sets whether the full dimension line should be displayed for linear diametric dimensions. |
| [GeneralDimensionType](../LinearGeneralDimension/LinearGeneralDimension_GeneralDimensionType.md) | Returns an enum indicating the type of general dimension. |
| [HideSecondArrowhead](../LinearGeneralDimension/LinearGeneralDimension_HideSecondArrowhead.md) | Gets and sets whether hide the second arrowhead of the dimension. |
| [HideValue](../LinearGeneralDimension/LinearGeneralDimension_HideValue.md) | Gets and sets the HideValue setting. |
| [IntentOne](../LinearGeneralDimension/LinearGeneralDimension_IntentOne.md) | Gets the sets first geometry associated with the dimension. |
| [IntentThree](../LinearGeneralDimension/LinearGeneralDimension_IntentThree.md) | Gets the sets the third geometry associated with the dimension. |
| [IntentTwo](../LinearGeneralDimension/LinearGeneralDimension_IntentTwo.md) | Gets the sets second geometry associated with the dimension. This may return Nothing in some cases where a single geometry was used for the dimension creation. |
| [IsBaselineSetMember](../LinearGeneralDimension/LinearGeneralDimension_IsBaselineSetMember.md) | Property that returns whether this dimension is a member of a baseline dimension set. If this property returns True, the BaselineDimensionSet object is returned by the BaselineDimensionSet property. |
| [IsChainSetMember](../LinearGeneralDimension/LinearGeneralDimension_IsChainSetMember.md) | Property that returns whether this dimension is a member of a chain dimension set. If this property returns True, the ChainDimensionSet object is returned by the ChainDimensionSet property. |
| [IsInspectionDimension](../LinearGeneralDimension/LinearGeneralDimension_IsInspectionDimension.md) | Gets and sets whether this is an inspection dimension. |
| [Layer](../LinearGeneralDimension/LinearGeneralDimension_Layer.md) | Gets and sets the layer applied to this dimension. |
| [ModelValue](../LinearGeneralDimension/LinearGeneralDimension_ModelValue.md) | Property that gets the dimension value as defined in the model or as measured in the drawing. |
| [ModelValueOverridden](../LinearGeneralDimension/LinearGeneralDimension_ModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. |
| [OverrideModelValue](../LinearGeneralDimension/LinearGeneralDimension_OverrideModelValue.md) | Gets and sets the NominalValue setting. |
| [Parent](../LinearGeneralDimension/LinearGeneralDimension_Parent.md) | Property that returns the parent sheet of the object. |
| [Precision](../LinearGeneralDimension/LinearGeneralDimension_Precision.md) | Gets and sets the Precision setting. |
| [Retrieved](../LinearGeneralDimension/LinearGeneralDimension_Retrieved.md) | Property that indicates whether the dimension was created as a result of retrieving it either from the model or a drawing view sketch. If True, the RetrievedFrom property returns the object that the dimension was retrieved from. |
| [RetrievedFrom](../LinearGeneralDimension/LinearGeneralDimension_RetrievedFrom.md) | Property that returns the object that this dimension was retrieved from. Possible return objects include all sketch constraint objects that derive from DimensionConstraint and their proxies, FeatureDimension and FeatureDimensionProxy. The property returns Nothing if the Retrieved property returns False. |
| [SecondArrowheadInside](../LinearGeneralDimension/LinearGeneralDimension_SecondArrowheadInside.md) | Read-write property that gets and sets whether the second arrowhead is inside or outside. |
| [SecondArrowheadPosition](../LinearGeneralDimension/LinearGeneralDimension_SecondArrowheadPosition.md) | Gets and sets the position of the second arrowhead. |
| [SecondArrowheadType](../LinearGeneralDimension/LinearGeneralDimension_SecondArrowheadType.md) | Read-write property that gets and sets the type of the second arrowhead. |
| [ShowLeader](../LinearGeneralDimension/LinearGeneralDimension_ShowLeader.md) | Gets and sets whether to display a leader line for the dimension text. |
| [Style](../LinearGeneralDimension/LinearGeneralDimension_Style.md) | Gets and sets the DimensionStyle associated with the dimension. |
| [Text](../LinearGeneralDimension/LinearGeneralDimension_Text.md) | Gets and sets the DimensionText setting. |
| [Tolerance](../LinearGeneralDimension/LinearGeneralDimension_Tolerance.md) | Property that returns the Tolerance object associated with this dimension. |
| [TolerancePrecision](../LinearGeneralDimension/LinearGeneralDimension_TolerancePrecision.md) | Gets and sets the precision of the tolerance text for the dimension. |
| [Type](../LinearGeneralDimension/LinearGeneralDimension_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [VirtualArcPosition](../LinearGeneralDimension/LinearGeneralDimension_VirtualArcPosition.md) | Gets and sets the geometry that defines the position of the virtual arc. |

## Accessed From

[BaselineDimensionSet.AddMember](../BaselineDimensionSet/BaselineDimensionSet_AddMember.md), [GeneralDimensions.AddArcLengthForeshortened](../GeneralDimensions/GeneralDimensions_AddArcLengthForeshortened.md), [GeneralDimensions.AddLinear](../GeneralDimensions/GeneralDimensions_AddLinear.md), [GeneralDimensions.AddLinear2](../GeneralDimensions/GeneralDimensions_AddLinear2.md), [GeneralDimensions.AddLinearForeshortened](../GeneralDimensions/GeneralDimensions_AddLinearForeshortened.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Center Dimension Text](../../sample-programs/AngularGeneralDimension_CenterText_Sample.md) | This sample demonstrates how to center the text of all dimensions on the active sheet in a drawing. |
| [Add surface texture symbol to dimension](../../sample-programs/SurfaceTextureSymbols_Add_Sample.md) | This sample demonstrates the creation of a surface texture symbol attached to the extension line of a drawing dimension. |

## Version

Introduced in version 11
