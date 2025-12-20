# GeneralDimension Object

Derived from: [DrawingDimension](../DrawingDimension/DrawingDimension.md) Object

## Description

The GeneralDimension object represents a general dimension placed on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../GeneralDimension/GeneralDimension_Delete.md) | Method that deletes the DrawingDimension. |
| [GetInspectionDimensionData](../GeneralDimension/GeneralDimension_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [GetReferenceKey](../GeneralDimension/GeneralDimension_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [PromoteToSketch](../GeneralDimension/GeneralDimension_PromoteToSketch.md) | Method that copies the dimension to the underlying sketch. This method only works for dimensions associated with a draft view. |
| [SetInspectionDimensionData](../GeneralDimension/GeneralDimension_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn't already. |
| [ShowAllExtensionLines](../GeneralDimension/GeneralDimension_ShowAllExtensionLines.md) | Method that un-hides all the extension lines associated with this dimension. If there are no hidden extension lines associated with this dimension, this method does nothing and returns a success. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GeneralDimension/GeneralDimension_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrowheadsInside](../GeneralDimension/GeneralDimension_ArrowheadsInside.md) | Gets and sets the ArrowheadsInside setting. |
| [Attached](../GeneralDimension/GeneralDimension_Attached.md) | Indicates whether this dimension is attached to anything. If not, it is considered orphaned and can be removed. |
| [AttributeSets](../GeneralDimension/GeneralDimension_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionLine](../GeneralDimension/GeneralDimension_DimensionLine.md) | Property that returns the dimension line geometry of the dimension. |
| [FirstArrowheadInside](../GeneralDimension/GeneralDimension_FirstArrowheadInside.md) | Read-write property that gets and sets whether the first arrowhead is inside or outside. |
| [FirstArrowheadType](../GeneralDimension/GeneralDimension_FirstArrowheadType.md) | Read-write property that gets and sets the type of the first arrowhead. |
| [GeneralDimensionType](../GeneralDimension/GeneralDimension_GeneralDimensionType.md) | Returns an enum indicating the type of general dimension. |
| [HideValue](../GeneralDimension/GeneralDimension_HideValue.md) | Gets and sets the HideValue setting. |
| [IsInspectionDimension](../GeneralDimension/GeneralDimension_IsInspectionDimension.md) | Gets and sets whether this is an inspection dimension. |
| [Layer](../GeneralDimension/GeneralDimension_Layer.md) | Gets and sets the layer applied to this dimension. |
| [ModelValue](../GeneralDimension/GeneralDimension_ModelValue.md) | Property that gets the dimension value as defined in the model or as measured in the drawing. |
| [ModelValueOverridden](../GeneralDimension/GeneralDimension_ModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. |
| [OverrideModelValue](../GeneralDimension/GeneralDimension_OverrideModelValue.md) | Gets and sets the NominalValue setting. |
| [Parent](../GeneralDimension/GeneralDimension_Parent.md) | Property that returns the parent sheet of the object. |
| [Precision](../GeneralDimension/GeneralDimension_Precision.md) | Gets and sets the Precision setting. |
| [Retrieved](../GeneralDimension/GeneralDimension_Retrieved.md) | Property that indicates whether the dimension was created as a result of retrieving it either from the model or a drawing view sketch. If True, the RetrievedFrom property returns the object that the dimension was retrieved from. |
| [RetrievedFrom](../GeneralDimension/GeneralDimension_RetrievedFrom.md) | Property that returns the object that this dimension was retrieved from. Possible return objects include all sketch constraint objects that derive from DimensionConstraint and their proxies, FeatureDimension and FeatureDimensionProxy. The property returns Nothing if the Retrieved property returns False. |
| [SecondArrowheadInside](../GeneralDimension/GeneralDimension_SecondArrowheadInside.md) | Read-write property that gets and sets whether the second arrowhead is inside or outside. |
| [SecondArrowheadType](../GeneralDimension/GeneralDimension_SecondArrowheadType.md) | Read-write property that gets and sets the type of the second arrowhead. |
| [Style](../GeneralDimension/GeneralDimension_Style.md) | Gets and sets the DimensionStyle associated with the dimension. |
| [Text](../GeneralDimension/GeneralDimension_Text.md) | Gets and sets the DimensionText setting. |
| [Tolerance](../GeneralDimension/GeneralDimension_Tolerance.md) | Property that returns the Tolerance object associated with this dimension. |
| [TolerancePrecision](../GeneralDimension/GeneralDimension_TolerancePrecision.md) | Gets and sets the precision of the tolerance text for the dimension. |
| [Type](../GeneralDimension/GeneralDimension_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeneralDimensions.Item](../GeneralDimensions/GeneralDimensions_Item.md), [GeneralDimensionsEnumerator.Item](../GeneralDimensionsEnumerator/GeneralDimensionsEnumerator_Item.md)

## Derived Classes

[AngularGeneralDimension](../AngularGeneralDimension/AngularGeneralDimension.md), [DiameterGeneralDimension](../DiameterGeneralDimension/DiameterGeneralDimension.md), [LinearGeneralDimension](../LinearGeneralDimension/LinearGeneralDimension.md), [RadiusGeneralDimension](../RadiusGeneralDimension/RadiusGeneralDimension.md)

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |