# Weld Data XML Formatting

### More Information on Weld Data XML Formatting

Both WeldBead and CosmeticWeld Objects will support  a read only
property WeldInfo, which will return an XML formatted string containing a
description of the Weld Object. The XML string will contain a variable number of
tags which describe the elements and properties of the Weld Object.

The first section of the XML string will contain information which
describes those properties which pertain to the weld as a whole. Following the
first section will be a variable number of <WeldInfoSide> tags, which will
contain information descriptive of individual welds comprising the weld
feature.   An example first section follows:

<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

 <WeldmentInfo cosmeticweld="false" standard="ANSI"
fieldweld="false" >
    <FeatureName>My
Weldment</FeatureName>

  <AllAroundType>FilletWeld</AllAroundType>

  <IdentLineType>IdentLineOtherSide</IdentLineType>

    <StaggerType>EnableMoveStagger</StaggerType>

    <Note enclosed="false">This is a note</Note>

  :
  :
  (one or more
<WeldInfoSide> tagged
elements
  :
 </WeldmentInfo>

This initial section contains standard XML file header information; it is
sufficient to include only the XML version and encoding
information.

The root level tag is the WeldmentInfo tag. This tag has
attributes cosmeticweld, standard, and fieldweld. The cosmeticweld tag takes on
values true or false; the true value indicates that the object is a
cosmetic weld, false indicates a weld bead. The standard property indicates
the standard under which the weld callout is created; this may take on values
ANSI, BSI, DIN, GB, ISO, or JIS. The fieldweld attribute indicates that this is
a weld performed in the field, this attribute may be either true or
false.
Elements of the root WeldmentInfo tag in the first section are
FeatureName, which describes the name applied to the Weldment Feature,
AllAroundType, which indicates that a single weld type has been applied
to both sides of the feature, IdentLineType, which indicates the
linetype of the identifier line (ISO and DIN only), StaggerType, which
indicates the method used to stagger the elements of a two sided callout, and
NoteEnclosed, which contains the note string included in the
callout and has a property enclosed, which indicates that the note string is
enclosed in a box in the callout.

A single weldment callout can be used to describe two physical welds.
These two welds are termed the �arrow side?and �other side?welds.
Additionally, the arrow side and other side welds may be composed of up to two
physical welds each. If a second weld exists on the arrow side, it is termed the
arrowside2 weld, if a second weld exists on the other side, it is termed the
other side2weld. Each of these four possible welds will be represented by a
WeldInfoSide element in the XML string. An example WeldInfoSide element
follows:

<WeldInfoSide side="arrow" weldtype="PermanentBackingStripWeld"
 extentsthruall="true" facesprojected="false" brazingweld="false"
 brazeclearance="0.125" secondfillet="true">

  <Angle>45.00 degrees</Angle>

  <ContourType offset="0.25 inches" method="H">Concave</ContourType>
    <Gap>4.5
inches</Gap>
    <Depth>0.25 inches</Depth>

    <Diameter>0.75</Diameter>

  <Height>0.75</Height>

  <Intermittent>

   <Number>5.00</Number>

   <Length>4.00 inches</Length>

   <Spacing>2.0 inches</Spacing>

   <Pitch>2.00 inches</Pitch>

  </Intermittent>
    <Gap>1.00
inches</Gap>
    <Middle>string</Middle>

    <Prefix>"string"</Prefix>

  <Size>23.00 inches</Size>

  <SmallLeg>22.02 inches</SmallLeg>

  <Thickness>2.5 inches</Thickness>

  <Root>0.50</Root>

  <RootGap>1.0</RootGap>

</WeldInfoSide>

The WeldInfoSide element has a variable number of attributes. The side attribute may
be arrow, other, arrow2, or other2. The weldtype may be any valid weld, examples include fillet, plug,
slot, etc. (All valid weld types are in the following table).

The extentsthruall attribute may be true
or false;
it is true when the weld is limited by the length of the edge or face alone,
it is false when limiting work planes have been specified.
The facesprojected attribute describes a situation where the weld is placed
at a position created by projecting a face onto another.
This attribute may be true or false.
The brazingweld attribute indicates that the weld is brazed (brazing is
accomplished by using a bronze alloy that is melted and adhered to the parent metal).
The attribute brazeclearance specifies the clearance for the braze.

The WeldInfoSide tag has a variable number of elements.
The Angle element specifies the angle between weldments, and includes the
units used for this measure. The ContourType element describes contour
information for the weld. It takes on values Flat, Concave, and Convex.

The attribute method describes the finish of the weld, and may take on
alphabetic values C, G, R, H, M or U. The attribute offset describes the depth of the weld finish.
The element Gap describes the distance between weldments.
The element Depth describes the depth of the weld.
The element Height specifies the height of the weld.

The element Intermittent contains information related to intermittent
welds; it contains a variable number of the following elements:
Number (number of welds),
Length ( length of the welds),
Spacing (space between welds), and
Pitch (center to center distance).

The gap element describes the space between weldments.
The middle element specifies the type of intersection to perform on the weld.
The Prefix element allows text before the weld callout.
The size element specifies the size of the weld.
The SmallLeg element specifies the thickness of the weld.
The Thickness element represents the thickness of the weld.
The Root element specifies the root thickness of the weld.
The RootGap element specifies
the gap for the weld.

XML documents usually omit elements and attributes which do not hold values or are not valid. Throughout
this discussion it has been noted that the number of elements and attributes included in the XML string
will be variable. In general, the XML string should follow the convention that invalid or empty tags
should not be written. For example, in the initial section, the IdentLineType
element is valid only for callouts under the DIN and ISO standards; this tag should not be included in
the XML string if the weldment is not created using one of these standards.

Additionally, the number of WeldInfoSide tags will depend on the number of
welds comprising the callout; most often there will be one weld, and therefore
one WeldInfoSide tag will appear in the string. It is possible to have up to
four WeldInfoSide tags in the XML formatted string,
however. A table describing which tags are valid by standard and weld type
follows.

| **ANSI** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Diameter | Small Leg | Depth | Size | Length | Number | Spacing | Pitch | Method | Contour | Angle | Root | Height | Brazing | Thickness |  | Gap | Secondary Fillet |
| Fillet |  | yes | no | yes | yes | no | no | yes | yes | yes | no |  |  |  |  |  |  |  |
| Plug |  | no | yes | yes | no | yes | yes | no | yes | yes | yes |  |  |  |  |  |  |  |
| Slot |  | no | yes | yes | yes | yes | no | yes | yes | yes | yes |  |  |  |  |  |  |  |
| Stud |  | no | no | yes | no | yes | yes | no | yes | yes | no |  |  |  |  |  |  |  |
| Spot/Projection |  | no | no | yes | yes | yes | no | no | yes | no | no |  |  |  |  |  |  |  |
| Spot on Ref Line |  | no | no | yes | no | yes | no | no | yes | yes | no |  |  |  |  |  |  |  |
| Seam |  | no | no | yes | yes | yes | no | yes | yes | yes | no |  |  |  |  |  |  |  |
| Back or Backing |  | no | no | yes | yes | no | no | yes | yes | no | no |  |  |  |  |  |  |  |
| Surfacing |  | no | no | yes | no | no | no | no | yes | yes | no |  |  |  |  |  |  |  |
| Flange Edge |  | no | no | no | yes | no | no | yes | yes | yes | no | yes | yes | yes | yes |  |  |  |
| Flange Corner |  | no | yes | no | yes | no | no | yes | yes | yes | no | no | yes | yes | yes |  |  | yes - must be ansi fillet |
| Square Groove |  | no | no | yes | yes | no | no | yes | yes | yes | yes | no | no | yes | no |  | yes | yes - must be ansi fillet |
| Scarf Groove |  |  | yes | yes | yes |  |  | yes |  | yes | yes |  |  | yes | yes |  |  | no |
| V Groove |  | no | no | no | yes | no | no | yes | yes | yes | yes | no | no | yes | no |  | yes | no |
| Bevel Groove |  | no | no | yes | no | no | no | yes | yes | yes | yes | no | no | yes | no |  | yes | no |
| U Groove |  | no | yes | yes | yes | no | no | yes | yes | yes | yes | no | no | yes | no |  | no | no |
| j Groove |  | no | yes | yes | yes | no | no | yes | yes | yes | yes | no | no | yes | no |  | yes | yes - must be ansi fillet |
| Flare V Groove |  | no | yes | yes | yes | no | no | yes | yes | yes | no | no | no | yes | no |  | yes | no |
| Flare Single Groove |  | no | yes | yes | yes | no | no | yes | yes | yes | yes | no | no | yes | no |  | yes | yes - must be ansi fillet |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Non Destructive Exam | test | either side | number |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Permanent Backing | contour |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Melt Through | size | angle | contour |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| consumable | contour |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **BSI, DIN, GB, ISO** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Diameter | Small Leg | Depth | Size | Length | Number | Spacing | Pitch | Method | Contour | Angle | Root | Height | Brazing | Thickness |  | Gap | Secondary Fillet |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| fillet |  | no | yes | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| plug |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| spot or projection |  | no | no | yes | no | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| spot on reference lint |  | no | no | yes | no | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| Seam |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| Seam on reference line |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| Back or Backing |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| Surfacing |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| Butt Weld |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| Square Butt |  | no | yes | no | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | yes - must be fillet |
| Bevel Butt |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | yes - must be fillet |
| V Butt |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| U Butt |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| J Butt |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | yes - must be fillet |
| Edge Weld |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| Fold Joint |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| Inclined Joint |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| Surface Joint |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| Steep Flanked V Butt |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| V Butt Broad Root |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | no |
| Bevel Butt Broad Root |  | no | no | yes | yes | yes | yes | no | no | yes | no | no | no | no | no |  | no | yes - must be fillet |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **JIS** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Diameter | Small Leg | Depth | Size | Length | Number | Spacing | Pitch | Method | Contour | Angle | Root | Height | Brazing | Thickness | width | Gap | Secondary Fillet |
| fillet | no | yes | no | yes | yes | yes | no | yes | yes | yes | no | no | no | no | no | no | no | no |
| plug and spot | yes | no | yes | no | yes | yes | no | yes | yes | yes | yes | no | no | no | no | no | no | no |
| spot and projection | no | no | no | yes | no | yes | no | yes | yes | yes | no | no | no | no | no | no | no | no |
| seam weld | no | no | no | yes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| bead | no | no | no | yes | yes | Number | no | yes | yes | yes | no | no | no | no | no | no | yes | no |
| cladding | no | no | no | yes | yes | Number | no | no | yes | yes | no | no | no | no | no | yes | no | no |
| double flange | no | no | no | no | yes | yes | no | yes | yes | yes | no | no | yes | no | no | no | yes | no |
| single flange | no | no | no | no | yes | yes | no | no | yes | yes | no | no | yes | no | no | no | yes | yes |
| square groove | no | no | no | no | yes | yes | no | yes | yes | yes | no | no | no | no | no | no | yes | yes |
| v groove | no | no | yes | no | yes | yes | no | yes | yes | yes | yes | no | no | no | no | no | yes | no |
| bevel groove | no | no | yes | no | yes | yes | no | yes | yes | yes | yes | no | no | no | no | no | yes | yes |
| u groove | no | no | yes | no | yes | yes | no | no | yes | yes | yes | no | no | no | no | no | yes | no |
| j groove | no | no | yes | no | yes | yes | no | yes | yes | yes | yes | no | no | no | no | no | yes | yes |
| Flare V Groove | no | no | yes | no | yes | yes | no | yes | yes | yes | yes | no | no | no | no | no | yes | no |
| Flare Single Groove | no | no | yes | no | yes | yes | no | yes | yes | yes | yes | no | no | no | no | no | yes | yes |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Non Destructive Exam | Test | Length | Number | Either Side |  |  |  |  |  |  |  |  |  |  |  |  |  |  |