# import streamlit as st

# # Set title of the Streamlit app
# st.title("Tableau Dashboard in Streamlit")

# # Embed Tableau dashboard using iframe
# tableau_url = "https://public.tableau.com/views/Dashboard_17227011304940/Dashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

# st.markdown(f"""
# <iframe src="{tableau_url}" width="100%" height="800" frameborder="0"></iframe>
# """, unsafe_allow_html=True)

#------------------------------------------------------------------------------------------------------------------
# import streamlit as st

# # Set title of the Streamlit app
# st.title("Tableau Dashboard in Streamlit")

# # Embed Tableau dashboard using iframe
# tableau_url = "https://public.tableau.com/views/Dashboard_17227011304940/Dashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
# st.components.v1.iframe(tableau_url, width=1000, height=800, scrolling=True)

#------------------------------------------------------------------------------------------------------------------

import streamlit as st

# Set title of the Streamlit app
st.title("Tableau Dashboard in Streamlit")

# Embed Tableau dashboard using HTML
html_string = """
<div class='tableauPlaceholder' id='viz1722701149593' style='position: relative'>
    <noscript>
        <a href='#'>
            <img alt='Dashboard ' src='https://public.tableau.com/static/images/Da/Dashboard_17227011304940/Dashboard/1_rss.png' style='border: none' />
        </a>
    </noscript>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='Dashboard_17227011304940/Dashboard' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https://public.tableau.com/static/images/Da/Dashboard_17227011304940/Dashboard/1.png' />
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
    var divElement = document.getElementById('viz1722701149593');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if (divElement.offsetWidth > 800) {
        vizElement.style.width = '1800px';
        vizElement.style.height = '927px';
    } else if (divElement.offsetWidth > 500) {
        vizElement.style.width = '1800px';
        vizElement.style.height = '927px';
    } else {
        vizElement.style.width = '100%';
        vizElement.style.height = '2327px';
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

st.components.v1.html(html_string, width=1800, height=927)
