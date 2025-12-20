# HoleThreadNote Object

Derived from: [DiameterGeneralDimension](../DiameterGeneralDimension/DiameterGeneralDimension.md) Object

## Description

The HoleThreadNote object represents either a hole note or a thread note on a sheet and derives from the DiameterGeneralDimension object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../HoleThreadNote/HoleThreadNote_Delete.md) | Method that deletes the DrawingDimension. |
| [GetInspectionDimensionData](../HoleThreadNote/HoleThreadNote_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [GetReferenceKey](../HoleThreadNote/HoleThreadNote_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [PromoteToSketch](../HoleThreadNote/HoleThreadNote_PromoteToSketch.md) | Method that copies the dimension to the underlying sketch. This method only works for dimensions associated with a draft view. |
| [SetInspectionDimensionData](../HoleThreadNote/HoleThreadNote_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn't already. |
| [ShowAllExtensionLines](../HoleThreadNote/HoleThreadNote_ShowAllExtensionLines.md) | Method that un-hides all the extension lines associated with this dimension. If there are no hidden extension lines associated with this dimension, this method does nothing and returns a success. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HoleThreadNote/HoleThreadNote_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrowheadsInside](../HoleThreadNote/HoleThreadNote_ArrowheadsInside.md) | Gets and sets the ArrowheadsInside setting. |
| [Attached](../HoleThreadNote/HoleThreadNote_Attached.md) | Indicates whether this dimension is attached to anything. If not, it is considered orphaned and can be removed. |
| [AttributeSets](../HoleThreadNote/HoleThreadNote_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionLine](../HoleThreadNote/HoleThreadNote_DimensionLine.md) | Property that returns the dimension line geometry of the dimension. |
| [Edge](../HoleThreadNote/HoleThreadNote_Edge.md) | Gets and sets the hole/thread edge associated with the note. |
| [ExtensionLineOne](../HoleThreadNote/HoleThreadNote_ExtensionLineOne.md) | Property that returns the first extension line of the dimension. |
| [ExtensionLineTwo](../HoleThreadNote/HoleThreadNote_ExtensionLineTwo.md) | Property that returns the second extension line of the dimension. |
| [FirstArrowheadInside](../HoleThreadNote/HoleThreadNote_FirstArrowheadInside.md) | Read-write property that gets and sets whether the first arrowhead is inside or outside. |
| [FirstArrowheadType](../HoleThreadNote/HoleThreadNote_FirstArrowheadType.md) | Read-write property that gets and sets the type of the first arrowhead. |
| [FormattedHoleThreadNote](../HoleThreadNote/HoleThreadNote_FormattedHoleThreadNote.md) | Gets and sets the fully formatted string that defines the contents of the hole/thread note. |
| [FormattedQuantityNote](../HoleThreadNote/HoleThreadNote_FormattedQuantityNote.md) | Gets and sets the fully formatted string that defines the quantity note. |
| [GeneralDimensionType](../HoleThreadNote/HoleThreadNote_GeneralDimensionType.md) | Returns an enum indicating the type of general dimension. |
| [HideValue](../HoleThreadNote/HoleThreadNote_HideValue.md) | Gets and sets the HideValue setting. |
| [Intent](../HoleThreadNote/HoleThreadNote_Intent.md) | Gets and sets the geometry associated with the dimension. |
| [IsHoleNote](../HoleThreadNote/HoleThreadNote_IsHoleNote.md) | Property that indicates if this note is for a hole or thread feature. Returns True if it is for a hole note. This is true even in the case where the hole is tapped and has threads. Returns False in the case where the note is for a thread feature. There is some difference in behavior between the two and this property provides a convenient way to determine the expected behavior. |
| [IsInspectionDimension](../HoleThreadNote/HoleThreadNote_IsInspectionDimension.md) | Gets and sets whether this is an inspection dimension. |
| [Layer](../HoleThreadNote/HoleThreadNote_Layer.md) | Gets and sets the layer applied to this dimension. |
| [LeaderFromCenter](../HoleThreadNote/HoleThreadNote_LeaderFromCenter.md) | Gets and sets whether the leader starts from the center of the arc or the circle. |
| [ModelValue](../HoleThreadNote/HoleThreadNote_ModelValue.md) | Property that gets the dimension value as defined in the model or as measured in the drawing. |
| [ModelValueOverridden](../HoleThreadNote/HoleThreadNote_ModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. |
| [OverrideModelValue](../HoleThreadNote/HoleThreadNote_OverrideModelValue.md) | Gets and sets the NominalValue setting. |
| [Parent](../HoleThreadNote/HoleThreadNote_Parent.md) | Property that returns the parent sheet of the object. |
| [Precision](../HoleThreadNote/HoleThreadNote_Precision.md) | Gets and sets the Precision setting. |
| [QuantityDefinition](../HoleThreadNote/HoleThreadNote_QuantityDefinition.md) | Gets and sets how the quantity value is set for the note. |
| [Retrieved](../HoleThreadNote/HoleThreadNote_Retrieved.md) | Property that indicates whether the dimension was created as a result of retrieving it either from the model or a drawing view sketch. If True, the RetrievedFrom property returns the object that the dimension was retrieved from. |
| [RetrievedFrom](../HoleThreadNote/HoleThreadNote_RetrievedFrom.md) | Property that returns the object that this dimension was retrieved from. Possible return objects include all sketch constraint objects that derive from DimensionConstraint and their proxies, FeatureDimension and FeatureDimensionProxy. The property returns Nothing if the Retrieved property returns False. |
| [RightHandedThread](../HoleThreadNote/HoleThreadNote_RightHandedThread.md) | Gets and sets whether to show RH for right handed thread. |
| [SecondArrowheadInside](../HoleThreadNote/HoleThreadNote_SecondArrowheadInside.md) | Read-write property that gets and sets whether the second arrowhead is inside or outside. |
| [SecondArrowheadType](../HoleThreadNote/HoleThreadNote_SecondArrowheadType.md) | Read-write property that gets and sets the type of the second arrowhead. |
| [SingleDimensionLine](../HoleThreadNote/HoleThreadNote_SingleDimensionLine.md) | Gets and sets whether to use a single dimension line. |
| [Style](../HoleThreadNote/HoleThreadNote_Style.md) | Gets and sets the DimensionStyle associated with the dimension. |
| [TapDrill](../HoleThreadNote/HoleThreadNote_TapDrill.md) | Gets and sets whether to set the hole note as tap drill type. |
| [Text](../HoleThreadNote/HoleThreadNote_Text.md) | Gets and sets the DimensionText setting. |
| [Tolerance](../HoleThreadNote/HoleThreadNote_Tolerance.md) | Property that returns the Tolerance object associated with this dimension. |
| [TolerancePrecision](../HoleThreadNote/HoleThreadNote_TolerancePrecision.md) | Gets and sets the precision of the tolerance text for the dimension. |
| [Type](../HoleThreadNote/HoleThreadNote_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseCustomThreadDesignation](../HoleThreadNote/HoleThreadNote_UseCustomThreadDesignation.md) | Gets and sets whether to use the custom thread designation, as defined in the Thread.xls spreadsheet for thread notes. |
| [UseDefaultFormat](../HoleThreadNote/HoleThreadNote_UseDefaultFormat.md) | Gets and sets whether to use the default format for hole notes. |
| [UsePartUnits](../HoleThreadNote/HoleThreadNote_UsePartUnits.md) | Gets and sets whether to use model units or the units specified by dimension style. |

## Accessed From

[HoleThreadNotes.Add](../HoleThreadNotes/HoleThreadNotes_Add.md), [HoleThreadNotes.Item](../HoleThreadNotes/HoleThreadNotes_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create thread note](../../sample-programs/HoleThreadNotes_Add_Sample.md) | This sample demonstrates the creation of a thread note on a drawing view. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |