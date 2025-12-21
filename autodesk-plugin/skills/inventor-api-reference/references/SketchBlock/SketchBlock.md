# SketchBlock Object

## Description

The SketchBlock object represents a sketch block instance within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchBlock/SketchBlock_Delete.md) | Method that deletes the sketch block. |
| [Edit](../SketchBlock/SketchBlock_Edit.md) | Method that activates the sketch block for editing by the user. |
| [ExitEdit](../SketchBlock/SketchBlock_ExitEdit.md) | Method that causes the sketch block to return from the edit mode and into the environment specified by the input argument. If the sketch block is not currently active (i.e. this is not the same block as returned by Application.ActiveEditObject property), then this method does nothing. |
| [Explode](../SketchBlock/SketchBlock_Explode.md) | Method that explodes the contents of the block and deletes the block instance. Note that the contents of the block are retained. |
| [GetCustomLineType](../SketchBlock/SketchBlock_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetObject](../SketchBlock/SketchBlock_GetObject.md) | Method that returns the corresponding object in the sketch block for the given object from it's definition. |
| [GetReferenceKey](../SketchBlock/SketchBlock_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchBlock/SketchBlock_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchBlock/SketchBlock_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchBlock/SketchBlock_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ChildBlocks](../SketchBlock/SketchBlock_ChildBlocks.md) | Property that returns an enumerator of SketchBlocks objects found directly under this sketch block. |
| [Color](../SketchBlock/SketchBlock_Color.md) | Gets and sets the color for the sketch block. Setting the property to Nothing restores the sketch block to the default color. |
| [ConstraintStatus](../SketchBlock/SketchBlock_ConstraintStatus.md) | Property that returns the constraint status of the sketch block. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus and kUnknownConstraintStatus. |
| [ContainingSketchBlock](../SketchBlock/SketchBlock_ContainingSketchBlock.md) | Property that returns the sketch block that in turn contains this sketch block. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property \returns Nothing if this sketch block does not belong to another sketch block and lives directly under a sketch. |
| [Definition](../SketchBlock/SketchBlock_Definition.md) | Property that returns the referenced sketch block definition. |
| [Exported](../SketchBlock/SketchBlock_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [Flexible](../SketchBlock/SketchBlock_Flexible.md) | Gets and sets whether this sketch block is flexible. |
| [HasReferenceComponent](../SketchBlock/SketchBlock_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [LineType](../SketchBlock/SketchBlock_LineType.md) | Gets and sets the line type override for the sketch block. |
| [LineWeight](../SketchBlock/SketchBlock_LineWeight.md) | Gets and sets the line weight override for the sketch block. |
| [Name](../SketchBlock/SketchBlock_Name.md) | Gets and sets name of the sketch block. |
| [Parent](../SketchBlock/SketchBlock_Parent.md) | Property that returns the parent sketch of the object. |
| [Position](../SketchBlock/SketchBlock_Position.md) | Gets and sets the position of the sketch block. |
| [ReferenceComponent](../SketchBlock/SketchBlock_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchBlock/SketchBlock_ReferencedEntity.md) | Property that returns the referenced sketch block, if there is one. Else, the property returns Nothing. |
| [SketchBlockPath](../SketchBlock/SketchBlock_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch block is found. The enumerator returns a count of 0 if the block lives directly under a sketch. The path does not include this sketch block itself. |
| [Transformation](../SketchBlock/SketchBlock_Transformation.md) | Gets and sets the transformation matrix for the sketch block. |
| [Type](../SketchBlock/SketchBlock_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../SketchBlock/SketchBlock_Visible.md) | Gets and sets whether this sketch block is visible. |

## Accessed From

[SketchArc.ContainingSketchBlock](../SketchArc/SketchArc_ContainingSketchBlock.md), [SketchArcProxy.ContainingSketchBlock](../SketchArcProxy/SketchArcProxy_ContainingSketchBlock.md), [SketchBlock.ContainingSketchBlock](../SketchBlock/SketchBlock_ContainingSketchBlock.md), [SketchBlock.ReferencedEntity](../SketchBlock/SketchBlock_ReferencedEntity.md), [SketchBlockProxy.ContainingSketchBlock](../SketchBlockProxy/SketchBlockProxy_ContainingSketchBlock.md), [SketchBlockProxy.NativeObject](../SketchBlockProxy/SketchBlockProxy_NativeObject.md), [SketchBlockProxy.ReferencedEntity](../SketchBlockProxy/SketchBlockProxy_ReferencedEntity.md), [SketchBlocks.Add](../SketchBlocks/SketchBlocks_Add.md), [SketchBlocks.AddByDefinition](../SketchBlocks/SketchBlocks_AddByDefinition.md), [SketchBlocks.Item](../SketchBlocks/SketchBlocks_Item.md), [SketchBlocksEnumerator.Item](../SketchBlocksEnumerator/SketchBlocksEnumerator_Item.md), [SketchCircle.ContainingSketchBlock](../SketchCircle/SketchCircle_ContainingSketchBlock.md), [SketchCircleProxy.ContainingSketchBlock](../SketchCircleProxy/SketchCircleProxy_ContainingSketchBlock.md), [SketchControlPointSpline.ContainingSketchBlock](../SketchControlPointSpline/SketchControlPointSpline_ContainingSketchBlock.md), [SketchControlPointSplineProxy.ContainingSketchBlock](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ContainingSketchBlock.md), [SketchEllipse.ContainingSketchBlock](../SketchEllipse/SketchEllipse_ContainingSketchBlock.md), [SketchEllipseProxy.ContainingSketchBlock](../SketchEllipseProxy/SketchEllipseProxy_ContainingSketchBlock.md), [SketchEllipticalArc.ContainingSketchBlock](../SketchEllipticalArc/SketchEllipticalArc_ContainingSketchBlock.md), [SketchEllipticalArcProxy.ContainingSketchBlock](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_ContainingSketchBlock.md), [SketchEntity.ContainingSketchBlock](../SketchEntity/SketchEntity_ContainingSketchBlock.md), [SketchEquationCurve.ContainingSketchBlock](../SketchEquationCurve/SketchEquationCurve_ContainingSketchBlock.md), [SketchEquationCurveProxy.ContainingSketchBlock](../SketchEquationCurveProxy/SketchEquationCurveProxy_ContainingSketchBlock.md), [SketchFixedSpline.ContainingSketchBlock](../SketchFixedSpline/SketchFixedSpline_ContainingSketchBlock.md), [SketchFixedSplineProxy.ContainingSketchBlock](../SketchFixedSplineProxy/SketchFixedSplineProxy_ContainingSketchBlock.md), [SketchImage.ContainingSketchBlock](../SketchImage/SketchImage_ContainingSketchBlock.md), [SketchImageProxy.ContainingSketchBlock](../SketchImageProxy/SketchImageProxy_ContainingSketchBlock.md), [SketchLine.ContainingSketchBlock](../SketchLine/SketchLine_ContainingSketchBlock.md), [SketchLineProxy.ContainingSketchBlock](../SketchLineProxy/SketchLineProxy_ContainingSketchBlock.md), [SketchOffsetSpline.ContainingSketchBlock](../SketchOffsetSpline/SketchOffsetSpline_ContainingSketchBlock.md), [SketchOffsetSplineProxy.ContainingSketchBlock](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_ContainingSketchBlock.md), [SketchPoint.ContainingSketchBlock](../SketchPoint/SketchPoint_ContainingSketchBlock.md), [SketchPointProxy.ContainingSketchBlock](../SketchPointProxy/SketchPointProxy_ContainingSketchBlock.md), [SketchSpline.ContainingSketchBlock](../SketchSpline/SketchSpline_ContainingSketchBlock.md), [SketchSplineHandle.ContainingSketchBlock](../SketchSplineHandle/SketchSplineHandle_ContainingSketchBlock.md), [SketchSplineHandleProxy.ContainingSketchBlock](../SketchSplineHandleProxy/SketchSplineHandleProxy_ContainingSketchBlock.md), [SketchSplineProxy.ContainingSketchBlock](../SketchSplineProxy/SketchSplineProxy_ContainingSketchBlock.md), [TextBox.ContainingSketchBlock](../TextBox/TextBox_ContainingSketchBlock.md), [TextBoxProxy.ContainingSketchBlock](../TextBoxProxy/TextBoxProxy_ContainingSketchBlock.md)

## Derived Classes

[SketchBlockProxy](../SketchBlockProxy/SketchBlockProxy.md)

## Version

Introduced in version 2010
