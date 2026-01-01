# Design View Data XML Formatting

### DesignView XML String

**Information stored for a Design View**

A design view captures the following display characteristics:

1. Component visibility (visible or not visible)
2. Sketch and work feature visibility (visible or not visible)
3. Component selectionstatus (enabled or not enabled)
4. Color and style characteristics applied in the assembly
5. Zoom magnification
6. Viewing angle

**How is this data defined via XML?**

The output XML string should be compared to the XML
output of the StreamLine translator. For example, open
an Inventor assembly file, and then invoke the
Streamline translator from the Inventor File/SaveCopy As
menu item. When the Inventor Save CopyAs dialog appears,
select StreamLine Assembly Packages(\*.amp) as the output type, with
the designview data option. The data in the DesignViewInfo string
can be compared to the design view data in the XML file produced
by the Streamline translator.

**DesignViewInfo XML tags**

The XML tags for the DesignViewInfo string are as follows:

|  |  |
| --- | --- |
| DesignViewInfo | This is the root tag. |
| DesignView | This is one of the design views in the designview database. |
| Camera | This is the camera information for the parent design view. |
| Occurrence | This is an object to which the design view applies camera, visible, and material overrides. |
| Path | This is the path to the occurrence, as seen in the browser. |
| Material | The material parameters applied to the occurrence. |

**Example**

Below is part of a sample DesignViewInfo XML string, demonstrating the use of these tags.

```
-<DesignViewInfo units="cm" designviewfilepath="C:\Autodesk\Inventor 10\Tutorial Files\final\_assy.idv">

- <DesignView name="Internal
Components">

 - <Camera width="14.1727"
height="13.9774">

 <UpVector x="-0.333333" y="0.666667"
z="-0.333333" />

 <CameraPosition x="15.2765" y="17.3914"
z="21.4982" />

<Target x="-1.33647" y="0.778433" z="4.88529"
/>

 </Camera>

 - <Occurrence visible="false"
enabled="true" colored="true">

 - <Path>

 <PathNode>vbody.ipt:1</PathNode>

 </Path>

- <Material alpha="0.5" shine="20">

 <Diffuse r="17.0001" g="193" b="84.0001"
/>

 <AmbientColor r="12.9999" g="147" b="63"
/>

 <EmissiveColor r="0" g="0" b="0"
/>

<SpecularColor r="80.0001" g="239" b="139"
/>

 </Material>

 </Occurrence>

- <Occurrence visible="true" enabled="true"
colored="true">

 - <Path>

 <PathNode>vnozzle.ipt:1</PathNode>

 </Path>

 - <Material alpha="1"
shine="20">

 <Diffuse r="1.99996" g="54.0001" b="210"
/>

 <AmbientColor r="1.00011" g="40.0001"
b="158" />

 <EmissiveColor r="0" g="0" b="0"
/>

 <SpecularColor r="66.0001" g="113" b="253"
/>

 </Material>

 </Occurrence>

 - <Occurrence visible="true" enabled="true"
colored="true">

 - <Path>

 <PathNode>knob.ipt:1</PathNode>

 </Path>

 - <Material alpha="1" shine="10">
<Diffuse r="109" g="120" b="138" />

 <AmbientColor r="109" g="120" b="138"
/>

 <EmissiveColor r="0" g="0" b="0"
/>

 <SpecularColor r="84.9999" g="84.9999"
b="133" />

 </Material> </Occurrence>
</DesignView>

 - <DesignView name="All Components
Displayed">

 - <Camera width="14.1727"
height="13.9774">

 <UpVector x="-0.408248" y="0.816497"
z="-0.408248" />

 <CameraPosition x="17.3029" y="19.4178"
z="23.5247" />

 <Target x="-1.33647" y="0.778433"
z="4.88529" />

 </Camera>

- <Occurrence visible="true" enabled="true"
colored="true">

 - <Path>

 <PathNode>vbody.ipt:1</PathNode>

 </Path>

 - <Material alpha="0.5"
shine="20">

 <Diffuse r="17.0001" g="193" b="84.0001"
/>

 <AmbientColor r="12.9999" g="147" b="63"
/>

 <EmissiveColor r="0" g="0" b="0"
/>

 <SpecularColor r="80.0001" g="239" b="139"
/>

 </Material>

 </Occurrence>

 - <Occurrence visible="true" enabled="true"
colored="true">

- <Path>

 <PathNode>vnozzle.ipt:1</PathNode>

 </Path>

 - <Material alpha="1"
shine="20">

 <Diffuse r="1.99996" g="54.0001" b="210"
/>

 <AmbientColor r="1.00011" g="40.0001"
b="158" />

 <EmissiveColor r="0" g="0" b="0"
/>

 <SpecularColor r="66.0001" g="113" b="253"
/>

 </Material>

 </Occurrence>

 - <Occurrence visible="true" enabled="true"
colored="true">

 - <Path>

 <PathNode>knob.ipt:1</PathNode>

 </Path>

 - <Material alpha="1" shine="10">

 <Diffuse r="109" g="120" b="138"/>

 <AmbientColor r="109" g="120" b="138"/>

 <EmissiveColor r="0" g="0" b="0"/>

 <SpecularColor r="84.9999" g="84.9999"
b="133" />

 </Material>

 </Occurrence>

</DesignView>

</DesignViewInfo>
```