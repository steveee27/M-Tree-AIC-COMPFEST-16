import streamlit as st

# Set title of the Streamlit app
st.title("Tableau Dashboard in Streamlit")

# Embed Tableau dashboard using HTML
html_string = """
<div class='tableauPlaceholder' id='viz1723134094546' style='position: relative'>
    <noscript>
        <a href='#'>
            <img alt='Dashboard 2 ' src='https://public.tableau.com/static/images/Da/Dashboard4_17231339847690/Dashboard2/1_rss.png' style='border: none' />
        </a>
    </noscript>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='Dashboard4_17231339847690/Dashboard2' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https://public.tableau.com/static/images/Da/Dashboard4_17231339847690/Dashboard2/1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
        <param name='filter' value='publish=yes' />
    </object>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1723134094546');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if (divElement.offsetWidth > 800) {
        vizElement.style.width = '900px';
        vizElement.style.height = '1827px';
    } else if (divElement.offsetWidth > 500) {
        vizElement.style.width = '900px';
        vizElement.style.height = '1827px';
    } else {
        vizElement.style.width = '100%';
        vizElement.style.height = '3877px';
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

st.components.v1.html(html_string, width=900, height=1827)
